from .interface.ApiInterface import ApiInterface


class Parameter(ApiInterface):
    """Handles getting and setting machine parameters."""

    def getMachineParameterValue(self, parameter_num: int) -> int:
        """Get the value of a machine parameter."""
        return self._call('GetMachineParameterValue', int(parameter_num))

    def setMachineParameter(self, addr: int, value: float):
        """Set a machine parameter to the given value."""
        return self._call('SetMachineParameter', int(addr), float(value))

    def __getitem__(self, item):
        return self.getMachineParameterValue(item)

    def __setitem__(self, key, value):
        self.setMachineParameter(key, value)
