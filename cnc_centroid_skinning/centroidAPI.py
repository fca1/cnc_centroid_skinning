# load Python.NET
import sys

from Axis import Axis
from Csr import Csr
from Dro import Dro
from Job import Job
from MessageWindow import MessageWindow
from Parameter import Parameter
from Pipe import Pipe
from Plc import PLc
from Screen import Screen
from State import State
from Sys import Sys
from Tool import Tool
from Wcs import Wcs
from interface.pythonnetAPIInterface import PythonnetAPIInterface


class CentroidApi:
    Axes = None
    sys = None
    csr = None
    axis = None
    dro = None
    job = None
    message_window = None
    parameter = None
    screen = None
    state = None
    tool = None
    wcs = None
    plc = None
    _pipe = None  # used for CncPipe

    """
    Class for getting and setting different system variables.
    Class for getting DRO data from CNC12.
    """

    def __init__(self, path_running, useVcpPipe: bool = False, timeout: int = 1):
        """

        :param path_running: path of CNC12 program.
        :param useVcpPipe: False by default.
        :param timeout: in sec.
        """
        self._interface = PythonnetAPIInterface(path_running, useVcpPipe, timeout)
        # managment of enums

        self.Axes = self._interface.cls.Axes
        # instance_name's relation between dll object and python
        self.sys = Sys(self._interface, 'system')
        self.csr = Csr(self._interface, 'csr')
        self.axis = Axis(self._interface, 'axis')
        self.dro = Dro(self._interface, 'dro')
        self.job = Job(self._interface, 'job')
        self.message_window = MessageWindow(self._interface, 'message_window')
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
        """
 	    Tells if the class instance was successfully constructed.
        """
        return self._pipe.isConstructed()

    @property
    def burst_mode(self)->bool:
        """ Sets if the skinning app is saving after every command or not. """
        return self._pipe.burst_mode

    @burst_mode.setter
    def burst_mode(self,enable:bool):
        """ Sets if the skinning app is saving after every command or not.  """
        self._pipe.burst_mode = enable



    @property
    def burstMode(self):
        return self._interface.skinning.BurstMode

    @burstMode.setter
    def burstMode(self, value):
        self._interface.skinning.BurstMode = bool(value)

    @staticmethod
    def getVersion():
        return "V0.5.30"


def detect_cnc(file_path_of_prg: str, *kargs):
    """
    :param file_path_of_prg:  (path where cncskinning.dll
    :return:
    """
    sk = CentroidApi(file_path_of_prg, *kargs)
    if sk.isConstructed():
        sys.stdout.write("cnc_centroid_skinning communicates... OK\n")
        return True
    else:
        sys.stderr.write(f"is CNC12 is launched ? given path is correct ? \n")
        return False
