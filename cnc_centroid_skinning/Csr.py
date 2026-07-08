from .cncenums import WCS
from .interface.ApiInterface import ApiInterface


class Csr(ApiInterface):
    """Contains methods for getting and setting CSR angles."""

    def getAngle(self, wcs: WCS = None) -> float:
        """Get the CSR angle for the active or specified WCS."""
        if wcs is not None:
            return self._call('GetAngle', 1 + int(wcs))
        else:
            return self._call('GetAngle')

    def setAngle(self, angle: float, wcs: WCS = None):
        """Set the CSR angle for the active or specified WCS."""
        if wcs is not None:
            # CentroidAPI expects WCS here as a 1-based integer.
            return self._call('SetAngle', 1 + int(wcs), float(angle))
        else:
            return self._call('SetAngle', float(angle))

    def disableCSR(self):
        """Disable the active CSR."""
        return self._call('DisableCSR')

    def ReenableCSR(self):
        """Re-enable a previously disabled CSR."""
        return self._call('ReenableCSR')

    def __getitem__(self, item):
        """Get the CSR angle for a WCS item."""
        assert WCS.WCS_1 <= item <= WCS.WCS_18
        return self.getAngle(item if item >= 1 else None)

    def __setitem__(self, item, angle):
        """Set the CSR angle for a WCS item."""
        assert 0 <= item <= 18
        self.setAngle(angle, item if item >= 1 else None)
