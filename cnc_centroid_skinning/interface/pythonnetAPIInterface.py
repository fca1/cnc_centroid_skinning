"""pythonnet bridge to CentroidAPI.dll."""


class PythonnetAPIInterface:

    def __init__(self, path_running, useVcpPipe: bool, timeout: int):
        from ..runtime import load_centroid_api

        self.cls = load_centroid_api(path_running)
        # attempt to instantiate pythonnet with CentroidAPI
        self._skinning = self.cls(useVcpPipe, timeout)
        self.path_running = path_running

    @property
    def skinning(self):
        return self._skinning
