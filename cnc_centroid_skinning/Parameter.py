from CncPipe import CncPipe
from centroidAPIInterface import CentroidAPIInterface


class Parameter(CncPipe):
    """Handles getting and setting of machine parameters"""

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("parameter", interface)

    def getMachineParameterValue(self, parameter_num: int) -> int:
        """:return:  the value of a machine parameter. """
        return self._call_interface('GetMachineParameterValue', int(parameter_num), 0)

    def setMachineParameter(self, addr: int, value: float):
        """Sets machine parameter to a given value. """
        return self._call_interface('SetMachineParameter', int(addr), float(value))

    def __getitem__(self, item):
        return self.getMachineParameterValue(item)

    def __setitem__(self, key, value):
        self.setMachineParameter(key, value)
