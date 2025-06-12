from cncenums import Viewport
from centroidAPIInterface import CentroidAPIInterface


class Screen:
    """Class to get screen and viewport info """

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    def getViewportInfo(self, viewport: Viewport) -> tuple:
        """:return: info from the  specified viewport """
        return self.interface("screen.GetViewportInfo", viewport, 0, 0)
