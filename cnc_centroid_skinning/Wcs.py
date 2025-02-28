from CncPipe import CncPipe
from centroidAPIInterface import CentroidAPIInterface
from enums import WCS, Axes


class Wcs(CncPipe):
    """	Class for getting and setting values involving work coordinate system"""

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("wcs",interface)


    def getActiveWcs(self) -> int:
        """:return:  the active wcs. """
        return self._call_interface('GetActiveWcs', 0)

    def getWorkpieceOrigin(self, axis: Axes, wcs: WCS = None):
        """:return:  Part-zero for the specified wcs and axis. """
        if wcs:
            return self._call_interface('GetWorkpieceOrigin', wcs, axis)
        else:
            return self._call_interface('GetWorkpieceOrigin', axis)

    def selectNextWcs(self):
        """Select the next wcs.
        """
        return self._call_interface('SelectNextWcs', False)

    def selectPrevWcs(self):
        """Select the previous wcs.
        """
        return self._call_interface('SelectNextWcs', False)

    def setWorkpieceOrigin(self, axis: Axes = None, wcs: WCS = None):
        """Attempt to set the Part-Zero for a specified axis and a specified WCS. """
        if wcs:
            if axis:
                return self._call_interface('SetWorkpieceOrigin', wcs, axis)
            else:
                return self._call_interface('SetWorkpieceOrigin', wcs)
        else:
            if axis:
                return self._call_interface('SetWorkpieceOrigin', axis)
            else:
                return self._call_interface('SetWorkpieceOrigin')

    def GetWorkpieceReference(self,ret:int,axis:int) ->float:
        """Get reference point from the return menu in the work coordinate settings."""
        return self._call_interface('GetWorkpieceReference', int(ret), int(axis))

    def SetWorkpieceReference(self,ret:int,axis:int,point:float):
        """Set reference point from the return menu in the work coordinate settings"""
        return self._call_interface('SetWorkpieceReference',int(ret),int(axis),float(point))
