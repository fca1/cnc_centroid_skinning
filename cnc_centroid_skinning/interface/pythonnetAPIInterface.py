# load Python.NET
# noinspection PyUnresolvedReferences
from System import Array
# noinspection PyUnresolvedReferences
from System import String, Char, Int32, Double, Decimal

from cnc_centroid_skinning import CNCPipe

"""
This class is used to wrap with the dll. 
"""


class PythonnetAPIInterface:

    def __init__(self, path_running, useVcpPipe: bool, timeout: int):
        self.cls = CNCPipe
        # attempt to instanciate pythonnet with CncSkinning
        self._skinning = self.cls(useVcpPipe, timeout)
        self.path_running = path_running

        pass

    @property
    def skinning(self):
        return self._skinning
