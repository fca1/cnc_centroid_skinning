from builtins import float

from CncPipe import CncPipe
from centroidAPIInterface import CentroidAPIInterface
from enums import Axes, Direction, Rate


class Axis(CncPipe):
    """Class for setting and getting axis info. """

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("axis", interface)

    def getAccelTime(self, axis: Axes) -> float:
        """
        Get the accel time for a given axis.
        :param axis: given axis
        :return: a time
        """
        return self._call_interface('GetAccelTime', axis)[1]

    def setAccelTime(self, axis: Axes, time: float):
        """Set the acceleration time for the given axis. """
        assert time > 0
        return self._call_interface('SetAccelTime', axis, float(time))

    def getDeadstartVelocity(self, axis: Axes) -> float:
        """:return: Get the deadstart velocity for a given axis. """
        return self._call_interface('GetDeadstartVelocity', axis)

    def setDeadstartVelocity(self, axis: Axes, velocity: float):
        """Set the deadstart velocity for the given axis. """
        return self._call_interface('SetDeadstartVelocity', axis, float(velocity))

    def getDeltaVMax(self, axis: Axes) -> float:
        """:return: Get the delta vmax for the specified axis. """
        return self._call_interface('GetDeltaVMax', axis)

    def setDeltaVMax(self, axis: Axes, delta_v_max: float):
        """Set the delta vmax for the specified axis. """
        return self._call_interface('SetDeltaVMax', axis, float(delta_v_max))

    def getRate(self, axis: Axes, jog_rate: Rate) -> float:
        """:return: Get rate for a given axis """
        return self._call_interface('GetRate', axis, jog_rate)

    def getPower(self, axis: Axes) -> float:
        """:return: Gets the power state for a specified axis. """
        return self._call_interface('GetRate', axis)


    def getLabel(self, axis: Axes) -> str:
        """Get the label for the given axis. """
        return self._call_interface('GetLabel', axis)

    def getLashComp(self, axis: Axes) -> float:
        """:return: Get the lash comp for an axis. """
        return self._call_interface('GetLashComp', axis)

    def getScrewPitch(self, axis: Axes) -> float:
        """:return: Get the screw pitch for an axis. """
        return self._call_interface('GetScrewPitch', axis)

    def setLabel(self, axis: Axes, label: str):
        """Set the label for a given axis. """
        assert len(label) == 1
        return self._call_interface('SetLabel', axis, label[0])

    def setLashComp(self, axis: Axes, value: float):
        """Set the lash comp for a given axis. """
        return self._call_interface('SetLashComp', axis, float(value))

    def setRate(self, axis: Axes, rate_type: Rate, rate: float):
        """Set the desired rate for the given axis. """
        return self._call_interface('SetRate', axis, rate_type, float(rate))

    def SetScrewPitch(self, axis: Axes, value: float):
        """Set the screw pitch for a given axis. """
        return self._call_interface('SetScrewPitch', axis, float(value))

    def getLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Gets the axis limits for a specified axis and direction. """
        return self._call_interface('GetLimit', axis, direction)

    def setLimit(self, axis: Axes, direction: Direction, value: float):
        """Set the axis limit for a specified axis and direction. """
        return self._call_interface('SetLimit', axis, direction, float(value))

    def getHomeLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Get the axis home limit for a specified axis and direction. """
        return self._call_interface('GetHomeLimit', axis, direction)

    def setHomeLimit(self, axis: Axes, direction: Direction, value: float):
        """Set the axis home limit for a specified axis and direction. """
        return self._call_interface('SetHomeLimit', axis, direction, float(value))

    def getAxisReversal(self, axis: Axes) -> bool:
        """:return: Get whether the axis is reversed or not. """
        return self._call_interface('GetAxisReversal', axis, False)

    def setAxisReversal(self, axis: Axes, is_axis_reversed: bool):
        """Set whether the axis is reversed or not. """
        return self._call_interface('SetAxisReversal', axis, bool(is_axis_reversed))

    def getCountsPerTurn(self, axis: Axes) -> float:
        """:return: Get motor counts per turn (i.e. steps per rev) """
        return self._call_interface('GetCountsPerTurn', axis)

    def setCountsPerTurn(self, axis: Axes, value: float):
        """Set motor counts per turn (i.e. steps per rev) """
        return self._call_interface('SetCountsPerTurn', axis, float(value))

    def getTravelLimit(self, axis: Axes, direction: Direction) -> float:
        """:return: Get the travel limit for a specified axis a specified direction. """
        return self._call_interface('GetTravelLimit', axis, direction)

    def setTravelLimit(self, axis: Axes, direction: Direction, value: float):
        """Set a travel limit for a specified axis a specified direction. """
        return self._call_interface('SetTravelLimit', axis, direction, float(value))



    def getScalesCounts(self, axis: Axes) -> float:
        """Get the counts that a specified axis will scale in."""
        """Set a travel limit for a specified axis a specified direction. """
        return self._call_interface('GetScalesCounts', axis)

    def getScalesDeadband(self, axis: Axes) -> float:
        """Get the deadband for scaling for a specified axis"""
        return self._call_interface('GetScalesDeadband', axis)

    def getScalesEnable(self, axis: Axes) -> bool:
        """Get if scaling enabled a specified axis."""
        return self._call_interface('GetScalesEnable', axis)


    def getScalesInput(self, axis: Axes) -> int:
        """Get the encoder input that is scaling a specified axis."""
        return self._call_interface('GetScalesInput', axis)


    def getScalesVelocity(self, axis: Axes) -> float:
        """Get the velocity for sclaing for a specified axis."""
        return self._call_interface('GetScalesVelocity', axis)


    def setScalesCounts(self, axis: Axes,scaling_counts:float):
        """"	Set the counts a specified axis will be scaled by"""
        return self._call_interface('SetScalesCounts', axis,float(scaling_counts))


    def setScalesDeadband(self, axis: Axes,value:int):
        """Set the deadband for scaling for a specified axis"""
        return self._call_interface('SetScalesDeadband', axis,int(value))

    def setScalesEnable(self, axis: Axes,enable:bool):
        """Set a scaling to be enabled for a specified axis"""
        return self._call_interface('SetScalesEnable', axis,bool(enable))

    def setScalesInput(self, axis: Axes,value:int):
        """Set a encoder input for scaling a specified axis"""
        return self._call_interface('SetScalesInput', axis,int(value))

    def setScalesVelocity(self, axis: Axes,value:float):
        """Set the velocity for scaling for a specified axis"""
        return self._call_interface('SetScalesVelocity', axis,float(value))
