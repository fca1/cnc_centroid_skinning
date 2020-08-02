# load Python.NET
import sys

import clr
# noinspection PyUnresolvedReferences
from System import String, Char, Int32, Double
# noinspection PyUnresolvedReferences
from System import Array

from .Axis import Axis
from .Csr import Csr
from .Dro import Dro
from .Job import Job
from .MessageWindow import MessageWindow
from .Parameter import Parameter
from .Plc import PLc
from .Screen import Screen
from .cncSkinningInterface import CncSkinningInterface
from .State import State
from .Sys import Sys
from .Tool import Tool
from .Wcs import Wcs


class CncSkinning(CncSkinningInterface):
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
        super().__init__(path_running, useVcpPipe, timeout)


        self.system = Sys(self)
        '''Class for getting and setting different system variables'''
        self.csr = Csr(self)
        '''Contains methods for getting and setting CSR angles'''
        self.axis = Axis(self)
        '''Class for setting and getting axis info'''
        self.dro = Dro(self)
        '''Class to get DRO information from CNC12'''
        self.job = Job(self)
        """A class for constructing and running jobs"""
        self.message_window = MessageWindow(self)
        '''Class for getting status window information'''
        self.parameter = Parameter(self)
        '''Handles getting and setting of machine parameters'''
        self.screen = Screen(self)
        """Class to get screen and viewport info"""
        self.state = State(self)
        """Holds info relating to system state, e.g. move mode, position mode, feedrate, spindle speed, etc"""
        self.tool = Tool(self)
        """Class to handle Mill Tool Info"""
        self.wcs = Wcs(self)
        """ Class for getting and setting values involving work coordinate system"""
        self.plc = PLc(self)
        """A class with functions related to PLC programming and state information"""

    def isConstructed(self) -> bool:
        """
 	    Tells if the class instance was successfully constructed.
        """
        return self('IsConstructed', wo_rc=True)

    @property
    def burstMode(self):
        return self._skinning.BurstMode

    @burstMode.setter
    def burstMode(self, value):
        self._skinning.BurstMode = bool(value)

    @staticmethod
    def getVersion():
        return "V1.0.0"


def detect_cnc(file_path_of_prg:str, *kargs):
    """
    :param file_path_of_prg:  (path where cncskinning.dll
    :return:
    """
    sk =  CncSkinning(file_path_of_prg, *kargs)
    if sk.isConstructed():
        sys.stdout.write("cnc_centroid_skinning communicates... OK\n")
        return True
    else:
        sys.stderr.write(f"is CNC12 is launched ? given path is correct ? \n")
        return False


if __name__ == "__main__":
    if len(sys.argv)<2:
        print("please, give in parameter the path of cncn/cnmt program")
        sys.exit(1)
    detect_cnc(sys.argv[1])