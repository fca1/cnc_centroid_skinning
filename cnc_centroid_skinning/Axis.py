from builtins import float

from .interface.ApiInterface import ApiInterface

from .cncenums import Axes, Direction, Rate


class Axis(ApiInterface):
    """Class for setting and getting axis info."""

    def getAccelTime(self, axis: Axes) -> float:
        """Get the acceleration time for the given axis."""
        return self._call('GetAccelTime', axis)

    def setAccelTime(self, axis: Axes, time: float):
        """Set the acceleration time for the given axis."""
        assert time > 0
        return self._call('SetAccelTime', axis, time)

    def getDeadstartVelocity(self, axis: Axes) -> float:
        """Get the deadstart velocity for the given axis."""
        return self._call('GetDeadstartVelocity', axis)

    def setDeadstartVelocity(self, axis: Axes, velocity: float):
        """Set the deadstart velocity for the given axis."""
        return self._call('SetDeadstartVelocity', axis, float(velocity))

    def getDeltaVMax(self, axis: Axes) -> float:
        """Get delta V max for the specified axis."""
        return self._call('GetDeltaVMax', axis)

    def setDeltaVMax(self, axis: Axes, delta_v_max: float):
        """Set delta V max for the specified axis."""
        return self._call('SetDeltaVMax', axis, float(delta_v_max))

    def getRate(self, axis: Axes, jog_rate: Rate) -> float:
        """Get the rate for the given axis."""
        return self._call('GetRate', axis, jog_rate)

    def getLabel(self, axis: Axes) -> str:
        """Get the label for the given axis."""
        return self._call('GetLabel', axis)

    def getLashComp(self, axis: Axes) -> float:
        """Get lash compensation for the given axis."""
        return self._call('GetLashComp', axis)

    def getScrewPitch(self, axis: Axes) -> float:
        """Get the screw pitch for the given axis."""
        return self._call('GetScrewPitch', axis)

    def setLabel(self, axis: Axes, label: str):
        """Set the label for the given axis."""
        assert len(label) == 1
        return self._call('SetLabel', axis, label[0])

    def setLashComp(self, axis: Axes, value: float):
        """Set lash compensation for the given axis."""
        return self._call('SetLashComp', axis, float(value))

    def setRate(self, axis: Axes, rate_type: Rate, rate: float):
        """Set the desired rate for the given axis."""
        return self._call('SetRate', axis, rate_type, float(rate))

    def SetScrewPitch(self, axis: Axes, value: float):
        """Set the screw pitch for the given axis."""
        return self._call('SetScrewPitch', axis, float(value))

    def getLimit(self, axis: Axes, direction: Direction) -> float:
        """Get the axis limit for a specified axis and direction."""
        return self._call('GetLimit', axis, direction)

    def setLimit(self, axis: Axes, direction: Direction, value: float):
        """Set the axis limit for a specified axis and direction."""
        return self._call('SetLimit', axis, direction, float(value))

    def getHomeLimit(self, axis: Axes, direction: Direction) -> float:
        """Get the axis home limit for a specified axis and direction."""
        return self._call('GetHomeLimit', axis, direction)

    def setHomeLimit(self, axis: Axes, direction: Direction, value: float):
        """Set the axis home limit for a specified axis and direction."""
        return self._call('SetHomeLimit', axis, direction, float(value))

    def getAxisReversal(self, axis: Axes) -> bool:
        """Return whether the axis is reversed."""
        return self._call('GetAxisReversal', axis)

    def setAxisReversal(self, axis: Axes, is_axis_reversed: bool):
        """Set whether the axis is reversed."""
        return self._call('SetAxisReversal', axis, bool(is_axis_reversed))

    def getCountsPerTurn(self, axis: Axes) -> float:
        """Get motor counts per turn."""
        return self._call('GetCountsPerTurn', axis)

    def setCountsPerTurn(self, axis: Axes, value: float):
        """Set motor counts per turn."""
        return self._call('SetCountsPerTurn', axis, float(value))

    def getTravelLimit(self, axis: Axes, direction: Direction) -> float:
        """Get the travel limit for a specified axis and direction."""
        return self._call('GetTravelLimit', axis, direction)

    def setTravelLimit(self, axis: Axes, direction: Direction, value: float):
        """Set a travel limit for a specified axis and direction."""
        return self._call('SetTravelLimit', axis, direction, float(value))
