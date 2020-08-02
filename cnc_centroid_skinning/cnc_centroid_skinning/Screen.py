from enum import IntEnum, unique

from .cncSkinningInterface import CncSkinningInterface


@unique
class Viewport(IntEnum):
    VIEWPORT_ACTIVE_G_CODES = 0
    """active g-codes display viewport"""
    VIEWPORT_DRO = 1
    """dro viewport"""
    VIEWPORT_FKEY = 2
    """The f-keys viewport"""
    VIEWPORT_MESSAGE = 3
    """message viewport """


class Screen:
    """Class to get screen and viewport info """
    def __init__(self, interface: CncSkinningInterface):
        self.interface = interface

    def getViewportInfo(self, viewport: Viewport) -> tuple:
        """:return: info from the  specified viewport """
        return self.interface("screen.GetViewportInfo", viewport.value, 0, 0)
