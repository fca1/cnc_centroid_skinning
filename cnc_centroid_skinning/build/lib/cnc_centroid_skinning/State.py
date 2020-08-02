from enum import IntEnum, unique
from typing import List, Tuple

from .cncSkinningInterface import CncSkinningInterface


@unique
class CircularInterpolationPlane(IntEnum):
    """The plane for circular interpolation commands. """
    XY = 0

    """G17 is the XY plane"""
    ZX = 1

    """G18 is the ZX plane"""
    YZ = 2

    """G19 is the YZ plane"""


class CircularInterpolationDirection(IntEnum):
    """The direction of a circular or helical interpolation. """
    CLOCKWISE = 0

    """Clockwise Arc."""
    COUNTERCLOCKWISE = 1

    """Counterclockwise Arc."""


class FeedHoldState(IntEnum):
    """An enumeration of possible feed hold states """
    FEED_HOLD_ON = 0
    """Feed hold button is pressed"""
    FEED_HOLD_OFF = 1
    """Feed hold button is not pressed"""
    UNKNOWN = 2
    """Feed hold status could not be determined."""


class MdiState(IntEnum):
    """Are we in MDI or not? """
    IN_MDI = 0
    """We are in Mdi"""
    NOT_IN_MDI = 1
    """We are not in Mdi"""
    UNKNOWN = 2
    """It is not known if we are in MDI or not."""


class MoveMode(IntEnum):
    """Enumerates the different move modes, namely, Rapid, Linear, Clockwis e -Arc, and Counterclockwis e -Arc """
    RAPID = 0
    """Rapid Motion (G0)"""
    LINEAR = 1
    """Linear Interpolation (G1)"""
    CW_ARC = 2
    """Clockwise Arc (G2)"""
    CCW_ARC = 3
    """Counterclockwise Arc (G3)"""
    UNKNOWN = 4
    """Indicates bad communication with the pipe to CNC12."""


class PositioningMode(IntEnum):
    """Enumerates the different positioning modes, namely, Absolute and Incremental """
    ABSOLUTE = 0
    """Absolute Positioning Mode (G90)"""
    INCREMENTAL = 1
    """Incremental Positioning Mode (G91)"""
    UNKNOWN = 2
    """Indicates bad communication with the pipe to CNC12."""


class UnitsOfMeasure(IntEnum):
    """Enumerates the different units of measure, namely, Imperial and Metric """
    INCH_UNITS = 0
    """Inch Units (G20)"""
    METRIC_UNITS = 1
    """Metric Units (G21)"""
    UNKNOWN = 2
    """Indicates a failure to communicate with CNC12"""


class Value(IntEnum):
    """Enumerates different values, maximum or minimum """
    MAX = 0
    """Maximum Value"""
    MIN = 1

    """Minimum Value"""


class HomingType(IntEnum):
    """Enumerates the different homing types: Jog, Home Switch, and Ref Mar k -HS. """
    JOG = 0
    """Jog Homing"""
    HOMESWITCH = 1
    """Home Switch Homing"""
    REFMARKHS = 2
    """Ref Mark-HS Homing"""
    UNKNOWN = 3
    """Unknown homing, usually an error."""


class State:
    """Holds info relating to system state, e.g. move mode, position mode, feedrate, spindle speed, etc """
    def __init__(self, interface: CncSkinningInterface):
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
        return FeedHoldState(self.interface('state.GetFeedHoldState', 0))

    def getGCodeDisplay(self) -> List[str]:
        """:return:  the list of g-code strings that usually displays on CNC12 when a job is running. """
        return list(map(str, self.interface('state.GetGCodeDisplay', [])))

    def getJobNameCurrent(self) -> str:
        """:return:  the name of the currently loaded job. """
        return self.interface('state.GetJobNameCurrent', '')

    def getMdiState(self) -> MdiState:
        return MdiState(self.interface('state.GetMdiState', 0))

    def getMoveMode(self) -> MoveMode:
        """:return:  the current move mode (rapid, linear, clockwise arc, counterclockwise arc) """
        return MoveMode(self.interface('state.GetMoveMode', 0))

    def getPositioningMode(self) -> PositioningMode:
        """:return:  the positioning mode of the machine currently. """
        return PositioningMode(self.interface('state.GetPositioningMode', 0))

    def getUnitsOfMeasureDefault(self) -> UnitsOfMeasure:
        """:return: s the default units of measure from CNC12 (Imperial or Metric) """
        return UnitsOfMeasure(self.interface('state.GetUnitsOfMeasureDefault', 0))

    def setImperialUnits(self):
        """Set the default uniot of measure to inch units. """
        return self.interface('state.SetImperialUnits')

    def setMetricUnits(self):
        """Set the default unit of measure to metric units """
        return self.interface('state.SetMetricUnits')

    def getUnitsOfMeasureDro(self) -> UnitsOfMeasure:
        """:return: s the dro units of measure from CNC12 (Imperial or Metric) """
        return UnitsOfMeasure(self.interface('state.GetUnitsOfMeasureDro', 0))

    def getFeedrate(self) -> float:
        """:return: the measured feedrate (accounts for feedrate override knob). """
        return self.interface('state.GetFeedrate', 0.0)

    def getSpindleSpeed(self) -> float:
        """:return:  the current spindle speed. """
        return self.interface('state.GetSpindleSpeed', 0.0)

    def getCurrentMachinePosition(self) -> Tuple[float]:
        """:return: s the current machine position. """
        return tuple(map(float, self.interface('state.GetCurrentMachinePosition', [])))

    def getFeedrateOverride(self) -> int:
        """:return:  the feedrate override as a percent between 1 and max (usually 120). """
        return self.interface('state.GetFeedrateOverride', 0)

    def getCurrentLocalPosition(self) -> Tuple[float]:
        """:return:  the current wcs position. """
        return tuple(map(float, self.interface('state.GetCurrentLocalPosition', [])))

    def getHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """:return:  the current Spindle Speed High Range maximum or minimum value. """
        return self.interface('state.GetHighRangeSpindleSpeed', max_or_min.value, 0.0)

    def setHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """Set the current Spindle Speed High Range maximum or minimum value. """
        return self.interface('state.SetHighRangeSpindleSpeed', max_or_min.value, 0.0)

    def getMachineHomeAtPowerUp(self) -> HomingType:
        """:return:  the currently set machine homing type at power up. """
        return HomingType(self.interface('state.GetMachineHomeAtPowerUp', 0))

    def setMachineHomeAtPowerUp(self, homing_type: HomingType):
        """Set the machine homing type at power up. """
        return self.interface('state.SetMachineHomeAtPowerUp', homing_type.value)
