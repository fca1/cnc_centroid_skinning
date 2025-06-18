from cncenums import WCS, Axes
from interface.ApiInterface import ApiInterface


class Wcs(ApiInterface):
    """	Class for getting and setting values involving work coordinate system"""

    def getActiveWcs(self) -> int:
        """:return:  the active wcs. """
        return self._call('GetActiveWcs', 0)

    def getWorkpieceOrigin(self, axis: Axes, wcs: WCS = None):
        """:return:  Part-zero for the specified wcs and axis. """
        if wcs:
            return self._call('GetWorkpieceOrigin', wcs, axis)
        else:
            return self._call('GetWorkpieceOrigin', axis)

    def selectNextWcs(self):
        """Select the next wcs.
        """
        return self._call('SelectNextWcs', False)

    def selectPrevWcs(self):
        """Select the previous wcs.
        """
        return self._call('SelectNextWcs', False)

    def setWorkpieceOrigin(self, axis: Axes = None, wcs: WCS = None):
        """Attempt to set the Part-Zero for a specified axis and a specified WCS. """
        if wcs:
            if axis:
                return self._call('SetWorkpieceOrigin', wcs, axis)
            else:
                return self._call('SetWorkpieceOrigin', wcs)
        else:
            if axis:
                return self._call('SetWorkpieceOrigin', axis)
            else:
                return self._call('SetWorkpieceOrigin')
