from Wcs import WCS
from interface.ApiInterface import ApiInterface


class Csr(ApiInterface):
    """	Contains methods for getting and setting CSR angles"""

    def getAngle(self, wcs: WCS = None) -> float:
        """Get the CSR angle for the CURRENTLY ACTIVE WCS. """
        if wcs is not None:
            return self._call('GetAngle', 1 + int(wcs))
        else:
            return self._call('GetAngle')

    def setAngle(self, angle: float, wcs: WCS = None):
        """Attempt to set the CSR angle for the specified WCS. """
        if wcs is not None:
            # TODO strange, why a int for the parameter wcs ?
            return self._call('SetAngle', 1 + int(wcs), float(angle))
        else:
            return self._call('SetAngle', float(angle))

    def disableCSR(self):
        """Disables the active CSR. CSR will reenable either when a job concludes or when ReenableCSR is called."""
        return self._call('DisableCSR')

    def ReenableCSR(self):
        """Enables a previously disabled CSR. Will return error if DisableCSR was never called or if CSR was reenabled via the conclusion of a job."""
        return self._call('ReenableCSR')

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
