from interface.ApiInterface import ApiInterface


class Parameter(ApiInterface):
    """Handles getting and setting of machine parameters"""


    def getMachineParameterValue(self, parameter_num: int) -> int:
        """:return:  the value of a machine parameter. """
        return self._call('parameter.GetMachineParameterValue', int(parameter_num), 0)

    def setMachineParameter(self, addr: int, value: float):
        """Sets machine parameter to a given value. """
        return self._call('parameter.SetMachineParameter', int(addr), float(value))

    def __getitem__(self, item):
        return self.getMachineParameterValue(item)

    def __setitem__(self, key, value):
        self.setMachineParameter(key, value)
