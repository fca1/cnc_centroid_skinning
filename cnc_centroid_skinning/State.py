from typing import List

from cncenums import MdiState, MoveMode, FeedHoldState, PositioningMode, UnitsOfMeasure, HomingType, Value
from interface.ApiInterface import ApiInterface


class State(ApiInterface):
    """Holds info relating to system state, e.g. move mode, position mode, feedrate, spindle speed, etc """

    def getScreenSize(self) -> tuple:
        """:return: the screen size of the CNC application. """
        return self._call('GetScreenSize', 0, 0)

    def getMonitorSize(self) -> tuple:
        """:return: the monitor size of the CNC application. """
        return self._call('GetMonitorSize', 0, 0)

    def getScreenPosition(self) -> tuple:
        """:return: the position of the CNC application. """
        return self._call('GetScreenPosition', 0, 0)

    def getAcornBoardRevision(self) -> int:
        """:return:  the Acorn Board Revision """
        return self._call('GetAcornBoardRevision', 0)

    def getActiveGCodes(self) -> List[str]:
        """:return:  the currently active modal G- and M- codes. """
        return list(map(str, self._call('GetActiveGCodes', [])))

    def getFeedHoldState(self) -> FeedHoldState:
        """:return:  the current feed hold state. """
        return self._call('GetFeedHoldState')

    def getGCodeDisplay(self) -> List[str]:
        """:return:  the list of g-code strings that usually displays on CNC12 when a job is running. """
        return list(map(str, self._call('GetGCodeDisplay', [])))

    def getJobNameCurrent(self) -> str:
        """:return:  the name of the currently loaded job. """
        return self._call('GetJobNameCurrent', '')

    def getMdiState(self) -> MdiState:
        return self._call('GetMdiState')

    def getMoveMode(self) -> MoveMode:
        """:return:  the current move mode (rapid, linear, clockwise arc, counterclockwise arc) """
        return self._call('GetMoveMode')

    def getPositioningMode(self) -> PositioningMode:
        """:return:  the positioning mode of the machine currently. """
        return self._call('GetPositioningMode')

    def getUnitsOfMeasureDefault(self) -> UnitsOfMeasure:
        """:return: s the default units of measure from CNC12 (Imperial or Metric) """
        return UnitsOfMeasure(int(self._call('GetUnitsOfMeasureDefault')))

    def setImperialUnits(self):
        """Set the default uniot of measure to inch units. """
        return self._call('SetImperialUnits')

    def setMetricUnits(self):
        """Set the default unit of measure to metric units """
        return self._call('SetMetricUnits')

    def getUnitsOfMeasureDro(self) -> UnitsOfMeasure:
        """:return: s the dro units of measure from CNC12 (Imperial or Metric) """
        return self._call('GetUnitsOfMeasureDro')

    def getFeedrate(self) -> float:
        """:return: the measured feedrate (accounts for feedrate override knob). """
        return self._call('GetFeedrate')

    def getSpindleSpeed(self) -> float:
        """:return:  the current spindle speed. """
        return self._call('GetSpindleSpeed')

    def getCurrentMachinePosition(self) -> [float,...]:
        """:return: s the current machine position. """
        machinePosition = self._call('GetCurrentMachinePosition', [])
        return tuple(map(float, machinePosition))

    def getFeedrateOverride(self) -> int:
        """:return:  the feedrate override as a percent between 1 and max (usually 120). """
        return self._call('GetFeedrateOverride')

    def getCurrentLocalPosition(self) -> [float]:
        """:return:  the current wcs position. """
        return tuple(map(float, self._call('GetCurrentLocalPosition', [])))

    def getHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """:return:  the current Spindle Speed High Range maximum or minimum value. """
        return self._call('GetHighRangeSpindleSpeed', max_or_min)

    def setHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """Set the current Spindle Speed High Range maximum or minimum value. """
        return self._call('SetHighRangeSpindleSpeed', max_or_min)

    def getMachineHomeAtPowerUp(self) -> HomingType:
        """:return:  the currently set machine homing type at power up. """
        return self._call('GetMachineHomeAtPowerUp')

    def setMachineHomeAtPowerUp(self, homing_type: HomingType):
        """Set the machine homing type at power up. """
        return self._call('SetMachineHomeAtPowerUp', homing_type)
