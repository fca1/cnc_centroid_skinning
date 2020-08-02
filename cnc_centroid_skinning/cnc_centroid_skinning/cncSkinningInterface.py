import sys
from typing import Tuple

# load Python.NET
import clr
# noinspection PyUnresolvedReferences
from System import String, Char, Int32, Double
# noinspection PyUnresolvedReferences
from System import Array

from .ReturnCode import ReturnCode
from .exceptions.SkinningException import ReturnCodeException

clr.AddReference('System.Collections')
# noinspection PyUnresolvedReferences
from System.Collections.Generic import Dictionary


class CncSkinningInterface:

    def __init__(self, path_running, useVcpPipe: bool, timeout: int):
        """
        Class constructor. If successful, it will open a pipe for communicating with CNC12.
        """
        assert timeout > 0
        sys.path.append(path_running)
        self._path_running = path_running
        clr.AddReference("CncSkinning")
        # noinspection PyUnresolvedReferences
        from CncSkinning import Skinning
        # attempt to instanciate pythonnet with CncSkinning
        self._skinning = Skinning(useVcpPipe, timeout)

    def __call__(self, *args, **kwargs) -> [Tuple, None]:
        def test_return_code(rvc):
            rc = ReturnCode(rvc)
            if rc != ReturnCode.SUCCESS:
                raise ReturnCodeException(f"Return Code returned by {fcnt}:={str(rc)}", rc)

        fcnt, *params = args
        leef = self._skinning
        for obj in fcnt.split("."):
            leef = getattr(leef, obj)
        ret_lst = leef(*params)
        if not kwargs.get('wo_rc', False):  # this option is used when return code is no waited
            # first item of list is a ReturnCode value. If No success raise an Exception
            rvc = ret_lst[0] if type(ret_lst) != int else ret_lst
            test_return_code(rvc)
            if type(ret_lst) == int:
                return None
            # return tuple only if there is more than one value to return
            ret_lst = ret_lst[1:] if type(ret_lst) == tuple else None
        return ret_lst[0] if (type(ret_lst) == tuple and len(ret_lst) == 1) else ret_lst
