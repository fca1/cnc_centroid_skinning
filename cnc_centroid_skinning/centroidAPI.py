import sys
from .interface.pythonnetAPIInterface import PythonnetAPIInterface


class CentroidApi:
    Axes = None
    sys = None
    csr = None
    axis = None
    dro = None
    job = None
    message_window = None
    inbound_communications = None
    inbound_comm = None
    parameter = None
    screen = None
    state = None
    tool = None
    wcs = None
    plc = None
    _pipe = None  # used for CncPipe

    """Top-level wrapper around CentroidAPI.CNCPipe."""

    def __init__(self, path_running, useVcpPipe: bool = False, timeout: int = 1):
        """Create a wrapper for the CNC12 installation path."""
        self._interface = PythonnetAPIInterface(path_running, useVcpPipe, timeout)
        from .Axis import Axis
        from .Csr import Csr
        from .Dro import Dro
        from .InboundComm import InboundComm
        from .Job import Job
        from .MessageWindow import MessageWindow
        from .Parameter import Parameter
        from .Pipe import Pipe
        from .Plc import PLc
        from .Screen import Screen
        from .State import State
        from .Sys import Sys
        from .Tool import Tool
        from .Wcs import Wcs

        # Expose root enum access for compatibility.

        self.Axes = self._interface.cls.Axes
        # Map Python wrappers to CNCPipe child objects.
        self.sys = Sys(self._interface, 'system')
        self.csr = Csr(self._interface, 'csr')
        self.axis = Axis(self._interface, 'axis')
        self.dro = Dro(self._interface, 'dro')
        self.job = Job(self._interface, 'job')
        self.message_window = MessageWindow(self._interface, 'message_window')
        self.inbound_communications = InboundComm(self._interface, 'inbound_communications')
        self.inbound_comm = self.inbound_communications
        self.parameter = Parameter(self._interface, 'parameter')
        self.screen = Screen(self._interface, 'screen')
        self.state = State(self._interface, 'state')
        self.tool = Tool(self._interface, 'tool')
        self.wcs = Wcs(self._interface, 'wcs')
        self.plc = PLc(self._interface, 'plc')
        self._pipe = Pipe(self._interface, '')
        pass
    @property
    def path_running(self):
        return self._interface.path_running

    def isConstructed(self) -> bool:
        """Return whether the CNCPipe instance was constructed successfully."""
        return self._pipe.isConstructed()

    @property
    def burst_mode(self)->bool:
        """Return whether burst mode is enabled."""
        return self._pipe.burst_mode

    @burst_mode.setter
    def burst_mode(self,enable:bool):
        """Set whether burst mode is enabled."""
        self._pipe.burst_mode = enable



    @property
    def burstMode(self):
        return self._interface.skinning.BurstMode

    @burstMode.setter
    def burstMode(self, value):
        self._interface.skinning.BurstMode = bool(value)

    @staticmethod
    def getVersion():
        return "V0.5.42"


def detect_cnc(file_path_of_prg: str, *kargs):
    """Return whether cnc_centroid_skinning can communicate with CNC12."""
    sk = CentroidApi(file_path_of_prg, *kargs)
    if sk.isConstructed():
        sys.stdout.write("cnc_centroid_skinning communicates... OK\n")
        return True
    else:
        sys.stderr.write("Is CNC12 running? Is the given path correct?\n")
        return False
