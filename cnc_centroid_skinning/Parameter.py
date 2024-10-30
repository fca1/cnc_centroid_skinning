from centroidAPIInterface import CentroidAPIInterface


class Parameter:
    """Handles getting and setting of machine parameters"""

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    def getMachineParameterValue(self, parameter_num: int) -> int:
        """:return:  the value of a machine parameter. """
        return self.interface('parameter.GetMachineParameterValue', int(parameter_num), 0)

    def setMachineParameter(self, addr: int, value: float):
        """Sets machine parameter to a given value. """
        return self.interface('parameter.SetMachineParameter', int(addr), float(value))

    def __getitem__(self, item):
        return self.getMachineParameterValue(item)

    def __setitem__(self, key, value):
        self.setMachineParameter(key, value)
