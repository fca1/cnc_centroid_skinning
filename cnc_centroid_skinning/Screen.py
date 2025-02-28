from CncPipe import CncPipe
from centroidAPIInterface import CentroidAPIInterface
from enums import Viewport


class Screen(CncPipe):
    """Class to get screen and viewport info """

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("screen",interface)

    def getViewportInfo(self, viewport: Viewport) -> tuple:
        """:return: info from the  specified viewport """
        return self._call_interface('GetViewportInfo', viewport, 0, 0)

