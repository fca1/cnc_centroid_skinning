from centroidAPIInterface import CentroidAPIInterface
from enums import WCS, Axes


class Wcs:
    """	Class for getting and setting values involving work coordinate system"""

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    def getActiveWcs(self) -> int:
        """:return:  the active wcs. """
        return self.interface('wcs.GetActiveWcs', 0)

    def getWorkpieceOrigin(self, axis: Axes, wcs: WCS = None):
        """:return:  Part-zero for the specified wcs and axis. """
        if wcs:
            return self.interface('wcs.GetWorkpieceOrigin', wcs, axis)
        else:
            return self.interface('wcs.GetWorkpieceOrigin', axis)

    def selectNextWcs(self):
        """Select the next wcs.
        """
        return self.interface('wcs.SelectNextWcs', False)

    def selectPrevWcs(self):
        """Select the previous wcs.
        """
        return self.interface('wcs.SelectNextWcs', False)

    def setWorkpieceOrigin(self, axis: Axes = None, wcs: WCS = None):
        """Attempt to set the Part-Zero for a specified axis and a specified WCS. """
        if wcs:
            if axis:
                return self.interface('wcs.SetWorkpieceOrigin', wcs, axis)
            else:
                return self.interface('wcs.SetWorkpieceOrigin', wcs)
        else:
            if axis:
                return self.interface('wcs.SetWorkpieceOrigin', axis)
            else:
                return self.interface('wcs.SetWorkpieceOrigin')
