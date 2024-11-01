from builtins import float


from enums import Axes, Direction, Rate
from centroidAPIInterface import CentroidAPIInterface


class Axis:
    """Class for setting and getting axis info. """

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    def getAccelTime(self, axis: Axes) -> float:
        """
        Get the accel time for a given axis.
        :param axis: given axis
        :return: a time
        """
        return self.interface('axis.GetAccelTime', axis)[1]

    def setAccelTime(self, axis: Axes, time: float):
        """Set the acceleration time for the given axis. """
        assert time > 0
        return self.interface('axis.SetAccelTime', axis, time)

    def getDeadstartVelocity(self, axis: Axes) -> float:
        """:return: Get the deadstart velocity for a given axis. """
        return self.interface('axis.GetDeadstartVelocity', axis)

    def setDeadstartVelocity(self, axis: Axes, velocity: float):
        """Set the deadstart velocity for the given axis. """
        return self.interface('axis.SetDeadstartVelocity', axis, float(velocity))

    def getDeltaVMax(self, axis: Axes) -> float:
        """:return: Get the delta vmax for the specified axis. """
        return self.interface('axis.GetDeltaVMax', axis)

    def setDeltaVMax(self, axis: Axes, delta_v_max: float):
        """Set the delta vmax for the specified axis. """
        return self.interface('axis.SetDeltaVMax', axis, float(delta_v_max))

    def getRate(self, axis: Axes, jog_rate: Rate) -> float:
        """:return: Get rate for a given axis """
        return self.interface('axis.GetRate', axis, jog_rate)

    def getLabel(self, axis: Axes) -> str:
        """Get the label for the given axis. """
        return self.interface('axis.GetLabel', axis)

    def getLashComp(self, axis: Axes) -> float:
        """:return: Get the lash comp for an axis. """
        return self.interface('axis.GetLashComp', axis)

    def getScrewPitch(self, axis: Axes) -> float:
        """:return: Get the screw pitch for an axis. """
        return self.interface('axis.GetScrewPitch', axis)

    def setLabel(self, axis: Axes, label: str):
        """Set the label for a given axis. """
        assert len(label) == 1
        return self.interface('axis.SetLabel', axis, label[0])

    def setLashComp(self, axis: Axes, value: float):
        """Set the lash comp for a given axis. """
        return self.interface('axis.SetLashComp', axis, float(value))

    def setRate(self, axis: Axes, rate_type: Rate, rate: float):
        """Set the desired rate for the given axis. """
        return self.interface('axis.SetRate', axis, rate_type, float(rate))

    def SetScrewPitch(self, axis: Axes, value: float):
        """Set the screw pitch for a given axis. """
        return self.interface('axis.SetScrewPitch', axis, float(value))

    def getLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Gets the axis limits for a specified axis and direction. """
        return self.interface('axis.GetLimit', axis, direction)

    def setLimit(self, axis: Axes, direction: Direction, value: float):
        """Set the axis limit for a specified axis and direction. """
        return self.interface('axis.SetLimit', axis, direction, float(value))

    def getHomeLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Get the axis home limit for a specified axis and direction. """
        return self.interface('axis.GetHomeLimit', axis, direction)

    def setHomeLimit(self, axis: Axes, direction: Direction, value: float):
        """Set the axis home limit for a specified axis and direction. """
        return self.interface('axis.SetHomeLimit', axis, direction, float(value))

    def getAxisReversal(self, axis: Axes) -> bool:
        """:return: Get whether the axis is reversed or not. """
        return self.interface('axis.GetAxisReversal', axis, False)

    def setAxisReversal(self, axis: Axes, is_axis_reversed: bool):
        """Set whether the axis is reversed or not. """
        return self.interface('axis.SetAxisReversal', axis, bool(is_axis_reversed))

    def getCountsPerTurn(self, axis: Axes) -> float:
        """:return: Get motor counts per turn (i.e. steps per rev) """
        return self.interface('axis.GetCountsPerTurn', axis)

    def setCountsPerTurn(self, axis: Axes, value: float):
        """Set motor counts per turn (i.e. steps per rev) """
        return self.interface('axis.SetCountsPerTurn', axis, float(value))

    def getTravelLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Get the travel limit for a specified axis a specified direction. """
        return self.interface('axis.GetTravelLimit', axis, direction)

    def setTravelLimit(self, axis: Axes, direction: Direction, value: float):
        """Set a travel limit for a specified axis a specified direction. """
        return self.interface('axis.SetTravelLimit', axis, direction, float(value))
