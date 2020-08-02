from builtins import float
from enum import IntEnum, unique

from .cncSkinningInterface import CncSkinningInterface
# noinspection PyUnresolvedReferences
from System import String, Char, Int32, Double



@unique
class Axes(IntEnum):
    """
    A list of axes
    """
    AXIS_1 = 0
    AXIS_2 = 1
    AXIS_3 = 2
    AXIS_4 = 3
    AXIS_5 = 4
    AXIS_6 = 5
    AXIS_7 = 6
    AXIS_8 = 7

@unique
class Rate(IntEnum):
    MAX = 0
    """
    Max rate
    """
    SLOW_JOG = 1
    """
    Slow Jog Rate
    """
    FAST_JOG = 2
    """
    ACORN ONLY Fast Jog Rate.
    """
    FAST_JOG_MINUS = 3
    """
    Fast Jog the negative direction
    """
    FAST_JOG_PLUS = 4
    """
    Fast jog the positive direction
    """


@unique
class Direction(IntEnum):
    PLUS = 0
    """
    Plus(positive)	direction.
    """
    MINUS = 1
    """
    Minus(negative)	direction.
    """


class Axis:
    """Class for setting and getting axis info. """
    def __init__(self, interface: CncSkinningInterface):
        self.interface = interface

    def getAccelTime(self, axis: Axes) -> float:
        """
        Get the accel time for a given axis.
        :param axis: given axis
        :return: a time
        """
        return self.interface('axis.GetAccelTime', axis.value, 0.0)[1]

    def setAccelTime(self, axis: Axes, time: float):
        """Set the acceleration time for the given axis. """
        assert time > 0
        return self.interface('axis.SetAccelTime', axis.value, time)

    def getDeadstartVelocity(self, axis: Axes) -> float:
        """:return: Get the deadstart velocity for a given axis. """
        return self.interface('axis.GetDeadstartVelocity', axis.value, 0.0)

    def setDeadstartVelocity(self, axis: Axes, velocity: float):
        """Set the deadstart velocity for the given axis. """
        return self.interface('axis.SetDeadstartVelocity', axis.value, float(velocity))

    def getDeltaVMax(self, axis: Axes) -> float:
        """:return: Get the delta vmax for the specified axis. """
        return self.interface('axis.GetDeltaVMax', axis.value, 0.0)

    def setDeltaVMax(self, axis: Axes, delta_v_max: float):
        """Set the delta vmax for the specified axis. """
        return self.interface('axis.SetDeltaVMax', axis.value, float(delta_v_max))

    def getRate(self, axis: Axes, jog_rate: Rate) -> float:
        """:return: Get rate for a given axis """
        return self.interface('axis.GetRate', axis.value, jog_rate.value, 0.0)

    def getLabel(self, axis: Axes) -> str:
        """Get the label for the given axis. """
        return self.interface('axis.GetLabel', axis.value, 0)

    def getLashComp(self, axis: Axes) -> float:
        """:return: Get the lash comp for an axis. """
        return self.interface('axis.GetLashComp', axis.value, 0.0)

    def getScrewPitch(self, axis: Axes) -> float:
        """:return: Get the screw pitch for an axis. """
        return self.interface('axis.GetScrewPitch', axis.value, 0.0)

    def setLabel(self, axis: Axes, label: str):
        """Set the label for a given axis. """
        assert len(label) == 1
        return self.interface('axis.SetLabel', axis.value, label[0])

    def setLashComp(self, axis: Axes, value: float):
        """Set the lash comp for a given axis. """
        return self.interface('axis.SetLashComp', axis.value, float(value))

    def setRate(self, axis: Axes, rate_type: Rate, rate: float):
        """Set the desired rate for the given axis. """
        return self.interface('axis.SetRate', axis.value, rate_type.value, float(rate))

    def SetScrewPitch(self, axis: Axes, value: float):
        """Set the screw pitch for a given axis. """
        return self.interface('axis.SetScrewPitch', axis.value, float(value))

    def getLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Gets the axis limits for a specified axis and direction. """
        return self.interface('axis.GetLimit', axis.value, direction.value, 0.0)

    def setLimit(self, axis: Axes, direction: Direction, value: float):
        """Set the axis limit for a specified axis and direction. """
        return self.interface('axis.SetLimit', axis.value, direction.value, float(value))

    def getHomeLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Get the axis home limit for a specified axis and direction. """
        return self.interface('axis.GetHomeLimit', axis.value, direction.value, 0.0)

    def setHomeLimit(self, axis: Axes, direction: Direction, value: float):
        """Set the axis home limit for a specified axis and direction. """
        return self.interface('axis.SetHomeLimit', axis.value, direction.value, float(value))

    def getAxisReversal(self, axis: Axes) -> bool:
        """:return: Get whether the axis is reversed or not. """
        return self.interface('axis.GetAxisReversal', axis.value, False)

    def setAxisReversal(self, axis: Axes, is_axis_reversed: bool):
        """Set whether the axis is reversed or not. """
        return self.interface('axis.SetAxisReversal', axis.value, bool(is_axis_reversed))

    def getCountsPerTurn(self, axis: Axes) -> float:
        """:return: Get motor counts per turn (i.e. steps per rev) """
        return self.interface('axis.GetCountsPerTurn', axis.value, 0.0)

    def setCountsPerTurn(self, axis: Axes, value: float):
        """Set motor counts per turn (i.e. steps per rev) """
        return self.interface('axis.SetCountsPerTurn', axis.value, float(value))

    def getTravelLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Get the travel limit for a specified axis a specified direction. """
        return self.interface('axis.GetTravelLimit', axis.value, direction.value, 0.0)

    def setTravelLimit(self, axis: Axes, direction: Direction, value: float):
        """Set a travel limit for a specified axis a specified direction. """
        return self.interface('axis.SetTravelLimit', axis.value, direction.value, float(value))
