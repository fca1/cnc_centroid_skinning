from cncenums import Viewport
from interface.ApiInterface import ApiInterface


class Screen(ApiInterface):
    """Class to get screen and viewport info """

    def getViewportInfo(self, viewport: Viewport) -> tuple:
        """:return: info from the  specified viewport """
        return self._call("GetViewportInfo", viewport, 0, 0)
