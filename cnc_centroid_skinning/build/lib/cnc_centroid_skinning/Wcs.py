from enum import IntEnum, unique

from . import Axes
from .cncSkinningInterface import CncSkinningInterface


@unique
class WCS(IntEnum):
    """Enumerates the various work coordinate systems. """
    WCS_1 = 0
    WCS_2 = 1
    WCS_3 = 2
    WCS_4 = 3
    WCS_5 = 4
    WCS_6 = 5
    WCS_7 = 6
    WCS_8 = 7
    WCS_9 = 8
    WCS_10 = 9
    WCS_11 = 10
    WCS_12 = 11
    WCS_13 = 12
    WCS_14 = 13
    WCS_15 = 14
    WCS_16 = 15
    WCS_17 = 16
    WCS_18 = 17
    WCS_UNKNOWN = 18


class Wcs:
    """	Class for getting and setting values involving work coordinate system"""
    def __init__(self, interface: CncSkinningInterface):
        self.interface = interface

    def getActiveWcs(self) -> int:
        """:return:  the active wcs. """
        return self.WCS(self.interface('wcs.GetActiveWcs', 0))

    def getWorkpieceOrigin(self, axis: Axes, wcs: WCS = None):
        """:return:  Part-zero for the specified wcs and axis. """
        if wcs:
            return self.interface('wcs.GetWorkpieceOrigin', wcs.value, axis.value, 0.0)
        else:
            return self.interface('wcs.GetWorkpieceOrigin', axis.value, 0.0)

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
                return self.interface('wcs.SetWorkpieceOrigin', wcs.value, axis.value)
            else:
                return self.interface('wcs.SetWorkpieceOrigin', wcs.value)
        else:
            if axis:
                return self.interface('wcs.SetWorkpieceOrigin', axis.value)
            else:
                return self.interface('wcs.SetWorkpieceOrigin')
