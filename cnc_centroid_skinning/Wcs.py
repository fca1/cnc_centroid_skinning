from .cncenums import WCS, Axes
from .interface.ApiInterface import ApiInterface


class Wcs(ApiInterface):
    """	Class for getting and setting values involving work coordinate system"""

    def getActiveWcs(self) -> int:
        """:return:  the active wcs. """
        return self._call('GetActiveWcs')

    def getWorkpieceOrigin(self, axis: Axes, wcs: WCS = None):
        """:return:  Part-zero for the specified wcs and axis. """
        if wcs:
            return self._call('GetWorkpieceOrigin', wcs, axis)
        else:
            return self._call('GetWorkpieceOrigin', axis)

    def selectNextWcs(self):
        """Select the next wcs.
        """
        return self._call('SelectNextWcs')

    def selectPrevWcs(self):
        """Select the previous wcs.
        """
        return self._call('SelectPrevWcs')

    def getWorkpieceReference(self, ret: int, axis: Axes):
        """Get a return-menu reference point for a specified axis."""
        assert 1 <= int(ret) <= 4
        return self._call('GetWorkpieceReference', int(ret), axis)

    def setWorkpieceReference(self, ret: int, axis: Axes, point: float):
        """Set a return-menu reference point for a specified axis."""
        assert 1 <= int(ret) <= 4
        return self._call('SetWorkpieceReference', int(ret), axis, float(point))

    def setWorkpieceLocation(self, axis: Axes, location: float, wcs: WCS = None):
        """Set part location for an axis on the active or specified WCS."""
        if wcs:
            return self._call('SetWorkpieceLocation', wcs, axis, float(location))
        return self._call('SetWorkpieceLocation', axis, float(location))

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
