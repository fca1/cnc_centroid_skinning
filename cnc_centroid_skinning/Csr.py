from Wcs import WCS
from centroidAPIInterface import CentroidAPIInterface


class Csr:
    """	Contains methods for getting and setting CSR angles"""

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    def getAngle(self, wcs: WCS = None) -> float:
        """Get the CSR angle for the CURRENTLY ACTIVE WCS. """
        if wcs is not None:
            return self.interface('csr.GetAngle', 1+int(wcs))
        else:
            return self.interface('csr.GetAngle')

    def setAngle(self, angle: float, wcs: WCS = None):
        """Attempt to set the CSR angle for the specified WCS. """
        if wcs is not None:
            # TODO strange, why a int for the parameter wcs ?
            return self.interface('csr.SetAngle', 1+int(wcs), float(angle))
        else:
            return self.interface('csr.SetAngle', float(angle))

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