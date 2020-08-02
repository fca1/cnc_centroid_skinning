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
from .SkinningInterface import _SkinningInterface
from .State import State
from .Sys import Sys
from .Tool import Tool
from .Wcs import Wcs


class Skinning(_SkinningInterface):
    def __init__(self, path_running, useVcpPipe: bool = False, timeout: int = 1):
        super().__init__(path_running, useVcpPipe, timeout)
        self.system = Sys(self)
        self.csr = Csr(self)
        self.axis = Axis(self)
        self.dro = Dro(self)
        self.job = Job(self)
        self.message_window = MessageWindow(self)
        self.parameter = Parameter(self)
        self.screen = Screen(self)
        self.state = State(self)
        self.tool = Tool(self)
        self.wcs = Wcs(self)
        self.plc = PLc(self)

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
    sk =  Skinning(file_path_of_prg,*kargs)
    if sk.isConstructed():
        print("py_cnc_skinning communicate")
        return True
    else:
        print(f"is cnct/cncm is running ?")
        return False


if __name__ == "__main__":
    if len(sys.argv)<2:
        print("please, give in parameter the path of cncn/cnmt program")
        sys.exit(1)
    detect_cnc(sys.argv[1])