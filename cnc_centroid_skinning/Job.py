from enum import IntEnum, unique
from typing import List

from CncPipe import CncPipe
from centroidAPIInterface import CentroidAPIInterface


@unique
class ProbeBossOrientation(IntEnum):
    X_PLUS = 0

    """Positive x direction."""
    Y_PLUS = 1

    """Positive y direction."""
    X_MINUS = 2

    """Negative x direction."""
    Y_MINUS = 3
    """Negative y direction."""


class Job(CncPipe):
    """A class for constructing and running jobs """

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("job",interface)
        
    def load(self, path: str):
        """Load an existing job into CNC12"""
        return self._call_interface('Load', path)

    def runCommand(self, command: str, require_cycle_start: bool = True):
        """
        Run a command now. If we require cycle start, it will post as an actual job
        .. warnings also::  If a previous runCommand is running, this call is ignored without advertizing.
        https://centroidcncforum.com/viewtopic.php?f=60&t=4607
        """
        return self._call_interface('RunCommand', command, self.interface.path_running, bool(require_cycle_start))

    @property
    def gcode(self):
        return ""

    @gcode.setter
    def gcode(self, gc: [str, List[str]]):
        """

        :param gc: str or list of str
        :return: None
        """
        if type(gc) != str:
            gc = '\n'.join(gc)
        self.runCommand(gc, require_cycle_start=False)

    def cancelExecution(self):
        """Cancel execution of a job. In the emulator/offline intercon, this will issue the escape key since the plc isn't running to accept the cycle cancel command."""
        return self._call_interface('CancelExecution')

    def 	continueExecution(self):
        """Continue execution of a job that is waiting at an M0/M200/M201 command. Machine Parameter 440 needs to be set to 256 for this call to return SUCCESS."""
        return self._call_interface('ContinueExecution')

    def 	getJobRepeatState(self) -> bool:
        """Get if job repeat is on or not."""
        return self._call_interface('GetJobRepeatState')

    def 	setJobRepeatState (self,repeat:bool):
        """Set the Job Repeat State to on or off."""
        return self._call_interface('SetJobRepeatState',int(repeat))

    def 	refreshGraph (self,refresh_rtg:bool):
        """Refresh the onscreen graph."""
        return self._call_interface('RefreshGraph',bool(refresh_rtg))

    def 	getPartCount (self)->int:
        """Get the currently set part count."""
        return self._call_interface('GetPartCount')

    def 	getPartNumber (self)->int:
        """Get the current part number."""
        return self._call_interface('GetPartNumber')

    def getSystemVariable(self,variable_number:int)->[str,float]:
        """(#1 - #299, #400 - #31999)"""
        return self._call_interface('GetSystemVariable',int(variable_number))

    def setSystemVariable(self,variable_number:int,value:[str,float]):
        """(#1 - #299, #400 - #31999)"""
        return self._call_interface('SetSystemVariable',int(variable_number),value)

