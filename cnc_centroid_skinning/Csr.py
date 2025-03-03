from CncPipe import CncPipe
from Wcs import WCS
from centroidAPIInterface import CentroidAPIInterface


class Csr(CncPipe):
    """	Contains methods for getting and setting CSR angles"""

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("csr", interface)

    def disableCSR(self):
        return self._call_interface('DisableCSR')

    def reenableCSR(self):
        return self._call_interface('ReenableCSR')

    def getAngle(self, wcs: WCS = None) -> float:
        """Get the CSR angle for the CURRENTLY ACTIVE WCS. """
        if wcs is not None:
            return self._call_interface('GetAngle', 1 + int(wcs))
        else:
            return self._call_interface('GetAngle')

    def setAngle(self, angle: float, wcs: WCS = None):
        """Attempt to set the CSR angle for the specified WCS. """
        # TODO strange, why a int for the parameter wcs ?
        return self._call_interface('SetAngle', *(1 + int(wcs), float(angle)) if wcs is not None else (float(angle),))

    def __getitem__(self, item):
        """
        :param item: specified WCS or currently active wcs if 0
        :return: Get the CSR angle
        """
        assert WCS.WCS_1 <= item <= WCS.WCS_18
        return self.getAngle(item if item >= 1 else None)

    def __setitem__(self, item, angle):
        """
        Attempt to set the CSR angle
        :param item: specified WCS or currently active wcs if 0
        :param angle:
        :return:
        """
        assert 0 <= item <= 18
        self.setAngle(angle, item if item >= 1 else None)
