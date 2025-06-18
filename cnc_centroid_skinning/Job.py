from typing import List

from interface.ApiInterface import ApiInterface


class Job(ApiInterface):
    """A class for constructing and running jobs """


    def load(self, path: str):
        """Load an existing job into CNC12"""
        return self._call('Load', path)

    def cancelExecution(self):
        """Cancel execution of a job."""
        return self._call('CancelExecution')

    def continueExecution(self):
        """Continue execution of a job that is waiting at an M0/M200/M201 command."""
        return self._call('ContinueExecution')

    def getJobRepeatState(self) -> bool:
        """Get if job repeat is on or not."""
        return self._call('GetJobRepeatState')

    def setJobRepeatState(self, state: bool):
        """Set the Job Repeat State to on or off."""
        return self._call('SetJobRepeatState', state)

    def refreshGraph(self):
        """Refresh the onscreen graph."""
        return self._call('RefreshGraph')

    def getPartCount(self, part_count: int):
        """Get the currently set part count."""
        return self._call('GetPartCount', part_count)

    def getPartNumber(self) -> int:
        """Get the currently set part count."""
        return self._call('GetPartNumber')

    def getSystemVariable(self, variable_number: int) -> int:
        """Gets system variable (#1 - #299, #400 - #31999)"""
        assert 1 <= variable_number <= 299
        assert 400 <= variable_number <= 31999
        return self._call('GetSystemVariable', variable_number)

    def getSystemVariable(self, variable_number: int) -> str:
        """Gets system variable (#300 - #399)"""
        assert 300 <= variable_number <= 399
        return self._call('GetSystemVariable', variable_number)

    def runCommand(self, command: str, require_cycle_start: bool = True):
        """
        Run a command now. If we require cycle start, it will post as an actual job
        .. warnings also::  If a previous runCommand is running, this call is ignored without advertizing.
        https://centroidcncforum.com/viewtopic.php?f=60&t=4607
        """
        return self._call('RunCommand', command, self.path_running, bool(require_cycle_start))

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
