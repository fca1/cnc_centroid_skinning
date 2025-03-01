from typing import List, Tuple

from CncPipe import CncPipe
from centroidAPIInterface import CentroidAPIInterface
from enums import MdiState, MoveMode, FeedHoldState, PositioningMode, UnitsOfMeasure, HomingType, Value, ConsoleTypes


class State(CncPipe):
    """Holds info relating to system state, e.g. move mode, position mode, feedrate, spindle speed, etc """

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("state",interface)




    def getScreenSize(self) -> tuple:
        """:return: the screen size of the CNC application. """
        return self._call_interface('GetScreenSize', 0, 0)

    def getMonitorSize(self) -> tuple:
        """:return: the monitor size of the CNC application. """
        return self._call_interface('GetMonitorSize', 0, 0)

    def getScreenPosition(self) -> tuple:
        """:return: the position of the CNC application. """
        return self._call_interface('GetScreenPosition', 0, 0)

    def getAcornBoardRevision(self) -> int:
        """:return:  the Acorn Board Revision """
        return self._call_interface('GetAcornBoardRevision', 0)

    def getActiveGCodes(self) -> List[str]:
        """:return:  the currently active modal G- and M- codes. """
        return list(map(str, self._call_interface('GetActiveGCodes', [])))

    def getFeedHoldState(self) -> FeedHoldState:
        """:return:  the current feed hold state. """
        return self._call_interface('GetFeedHoldState')

    def getGCodeDisplay(self) -> List[str]:
        """:return:  the list of g-code strings that usually displays on CNC12 when a job is running. """
        return list(map(str, self._call_interface('GetGCodeDisplay', [])))

    def getJobNameCurrent(self) -> str:
        """:return:  the name of the currently loaded job. """
        return self._call_interface('GetJobNameCurrent', '')

    def getMdiState(self) -> MdiState:
        return self._call_interface('GetMdiState')

    def getMoveMode(self) -> MoveMode:
        """:return:  the current move mode (rapid, linear, clockwise arc, counterclockwise arc) """
        return self._call_interface('GetMoveMode')

    def getPositioningMode(self) -> PositioningMode:
        """:return:  the positioning mode of the machine currently. """
        return self._call_interface('GetPositioningMode')

    def getUnitsOfMeasureDefault(self) -> UnitsOfMeasure:
        """:return: s the default units of measure from CNC12 (Imperial or Metric) """
        return UnitsOfMeasure(int(self._call_interface('GetUnitsOfMeasureDefault')))

    def setImperialUnits(self):
        """Set the default uniot of measure to inch units. """
        return self._call_interface('SetImperialUnits')

    def setMetricUnits(self):
        """Set the default unit of measure to metric units """
        return self._call_interface('SetMetricUnits')

    def getUnitsOfMeasureDro(self) -> UnitsOfMeasure:
        """:return: s the dro units of measure from CNC12 (Imperial or Metric) """
        return self._call_interface('GetUnitsOfMeasureDro')

    def getFeedrate(self) -> float:
        """:return: the measured feedrate (accounts for feedrate override knob). """
        return self._call_interface('GetFeedrate')

    def getSpindleSpeed(self) -> float:
        """:return:  the current spindle speed. """
        return self._call_interface('GetSpindleSpeed')

    def getCurrentMachinePosition(self) -> Tuple[float]:
        """:return: s the current machine position. """
        return tuple(map(float, self._call_interface('GetCurrentMachinePosition')))

    def getFeedrateOverride(self) -> int:
        """:return:  the feedrate override as a percent between 1 and max (usually 120). """
        return self._call_interface('GetFeedrateOverride')

    def getUsbOnlineBits(self) -> Tuple[bool]:
        x = self._call_interface('GetUsbOnlineBits',[])


    def getCurrentLocalPosition(self) -> Tuple[float]:
        """:return:  the current wcs position. """
        return tuple(map(float, self._call_interface('GetCurrentLocalPosition')))

    def getHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """:return:  the current Spindle Speed High Range maximum or minimum value. """
        return self._call_interface('GetHighRangeSpindleSpeed', max_or_min)

    def setHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """Set the current Spindle Speed High Range maximum or minimum value. """
        return self._call_interface('SetHighRangeSpindleSpeed', max_or_min)

    def getMachineHomeAtPowerUp(self) -> HomingType:
        """:return:  the currently set machine homing type at power up. """
        return self._call_interface('GetMachineHomeAtPowerUp')

    def setMachineHomeAtPowerUp(self, homing_type: HomingType):
        """Set the machine homing type at power up. """
        return self._call_interface('SetMachineHomeAtPowerUp', homing_type)





    def getConsoleType(self) -> ConsoleTypes:
        """Get the current console type."""
        return self._call_interface('getConsoleType')

    def getCurrentLineInfo(self) -> (int,int,int):
        """Get the current line number of the executing job"""
        return self._call_interface('GetCurrentLineInfo')


    def getCurrentStackLevelZeroLineInfo(self) -> (int,int):
        """Get the current line number of the orginal executing job excludes calls to marcos"""
        return self._call_interface('GetCurrentStackLevelZeroLineInfo')

    def getFullPathJobNameCurrent(self) -> str:
        """Get the full pathname of the currently loaded job"""
        return self._call_interface('GetFullPathJobNameCurrent')

    def getJogState(self) -> bool:
        """Get if the user is jogging the machine or not."""
        return self._call_interface('GetJogState')

    def getUsbInputInversions(self) -> str:
        """Get the current USB-BOB input inversion bits."""
        return self._call_interface('GetUsbInputInversions')

    def isAPIRestricted(self)->bool:
        """Checks if all API calls are restricted in any way (CNC12 Running a job, in a menu that doesn't accept calls,
        etc.) Note that not every API call is restricted by the state of CNC12"""
        return self._call_interface('IsAPIRestricted')

    def isPCPoweringOff(self)->bool:
        """Checks if CNC12 triggered a shutdown of the computer."""
        return self._call_interface('IsPCPoweringOff')

    def setConsoleType(self,tpe: ConsoleTypes):
        return self._call_interface('SetConsoleType',tpe)


    def setDroImperialUnits(self):
        return self._call_interface('SetDroImperialUnits')

    def setDroMetricUnits(self):
        return self._call_interface('SetDroMetricUnits')

    def setPlasmaInterruptPoint(self,interrupt_x:float,interrupt_y:float):
        return self._call_interface('SetPlasmaInterruptPoint',float(interrupt_x),float(interrupt_y))

    def setUsbInputInversions(self,inversion:str):
        return self._call_interface('SetUsbInputInversions',inversion)

    def toggleUsbInputInversionBit(self,inversion:int):
        return self._call_interface('ToggleUsbInputInversionBit',inversion)

