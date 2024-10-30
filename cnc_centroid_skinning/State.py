from typing import List, Tuple

from enums import MdiState, MoveMode, FeedHoldState, PositioningMode, UnitsOfMeasure, HomingType, Value
from centroidAPIInterface import CentroidAPIInterface


class State:
    """Holds info relating to system state, e.g. move mode, position mode, feedrate, spindle speed, etc """

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    def getScreenSize(self) -> tuple:
        """:return: the screen size of the CNC application. """
        return self.interface('state.GetScreenSize', 0, 0)

    def getMonitorSize(self) -> tuple:
        """:return: the monitor size of the CNC application. """
        return self.interface('state.GetMonitorSize', 0, 0)

    def getScreenPosition(self) -> tuple:
        """:return: the position of the CNC application. """
        return self.interface('state.GetScreenPosition', 0, 0)

    def getAcornBoardRevision(self) -> int:
        """:return:  the Acorn Board Revision """
        return self.interface('state.GetAcornBoardRevision', 0)

    def getActiveGCodes(self) -> List[str]:
        """:return:  the currently active modal G- and M- codes. """
        return list(map(str, self.interface('state.GetActiveGCodes', [])))

    def getFeedHoldState(self) -> FeedHoldState:
        """:return:  the current feed hold state. """
        return self.interface('state.GetFeedHoldState')

    def getGCodeDisplay(self) -> List[str]:
        """:return:  the list of g-code strings that usually displays on CNC12 when a job is running. """
        return list(map(str, self.interface('state.GetGCodeDisplay', [])))

    def getJobNameCurrent(self) -> str:
        """:return:  the name of the currently loaded job. """
        return self.interface('state.GetJobNameCurrent', '')

    def getMdiState(self) -> MdiState:
        return self.interface('state.GetMdiState')

    def getMoveMode(self) -> MoveMode:
        """:return:  the current move mode (rapid, linear, clockwise arc, counterclockwise arc) """
        return self.interface('state.GetMoveMode')

    def getPositioningMode(self) -> PositioningMode:
        """:return:  the positioning mode of the machine currently. """
        return self.interface('state.GetPositioningMode')

    def getUnitsOfMeasureDefault(self) -> UnitsOfMeasure:
        """:return: s the default units of measure from CNC12 (Imperial or Metric) """
        return UnitsOfMeasure(int(self.interface('state.GetUnitsOfMeasureDefault')))

    def setImperialUnits(self):
        """Set the default uniot of measure to inch units. """
        return self.interface('state.SetImperialUnits')

    def setMetricUnits(self):
        """Set the default unit of measure to metric units """
        return self.interface('state.SetMetricUnits')

    def getUnitsOfMeasureDro(self) -> UnitsOfMeasure:
        """:return: s the dro units of measure from CNC12 (Imperial or Metric) """
        return self.interface('state.GetUnitsOfMeasureDro')

    def getFeedrate(self) -> float:
        """:return: the measured feedrate (accounts for feedrate override knob). """
        return self.interface('state.GetFeedrate')

    def getSpindleSpeed(self) -> float:
        """:return:  the current spindle speed. """
        return self.interface('state.GetSpindleSpeed')

    def getCurrentMachinePosition(self) -> Tuple[float]:
        """:return: s the current machine position. """
        return tuple(map(float, self.interface('state.GetCurrentMachinePosition', [])))

    def getFeedrateOverride(self) -> int:
        """:return:  the feedrate override as a percent between 1 and max (usually 120). """
        return self.interface('state.GetFeedrateOverride')

    def getCurrentLocalPosition(self) -> Tuple[float]:
        """:return:  the current wcs position. """
        return tuple(map(float, self.interface('state.GetCurrentLocalPosition', [])))

    def getHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """:return:  the current Spindle Speed High Range maximum or minimum value. """
        return self.interface('state.GetHighRangeSpindleSpeed', max_or_min)

    def setHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """Set the current Spindle Speed High Range maximum or minimum value. """
        return self.interface('state.SetHighRangeSpindleSpeed', max_or_min)

    def getMachineHomeAtPowerUp(self) -> HomingType:
        """:return:  the currently set machine homing type at power up. """
        return self.interface('state.GetMachineHomeAtPowerUp')

    def setMachineHomeAtPowerUp(self, homing_type: HomingType):
        """Set the machine homing type at power up. """
        return self.interface('state.SetMachineHomeAtPowerUp', homing_type)
