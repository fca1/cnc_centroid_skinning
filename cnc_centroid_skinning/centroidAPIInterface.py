from typing import Tuple

# load Python.NET
# noinspection PyUnresolvedReferences
from System import Array
# noinspection PyUnresolvedReferences
from System import String, Char, Int32, Double, Decimal

from cnc_centroid_skinning import CNCPipe
from enums import ReturnCode
from exceptions.SkinningException import ReturnCodeException

"""
This class is used to wrap with the dll. 
"""
class CentroidAPIInterface:

    def __init__(self, path_running, useVcpPipe: bool, timeout: int):
        self._cls = CNCPipe
        # attempt to instanciate pythonnet with CncSkinning
        self.skinning = self._cls(useVcpPipe, timeout)
        self.path_running = path_running

        pass

    def __call__(self, *args, **kwargs) -> [Tuple, None]:
        def test_return_code(_rvc):
            rc = ReturnCode(int(_rvc))
            if rc != ReturnCode.SUCCESS:
                raise ReturnCodeException(f"Return Code returned by {fcnt}:={str(rc)}", rc)



        fcnt, *params = args
        leef = self.skinning
        for obj in fcnt.split("."):
            leef = getattr(leef, obj)
        # Transform float with Double  ( python float -> .net Double)
        params = [Double(i) if isinstance(i,float) else i  for i in params ]
        # Call the method found (pythonnet works between .net and python)
        try:
            ret_lst = leef(*params)
        except Exception as e:
            raise ReturnCodeException("bad call parameters",ReturnCode.ERROR_UNKNOWN)
        if not kwargs.get('wo_rc', False):  # this option is used when return code is no waited
            # first item of list is a ReturnCode value. If No success raise an Exception
            rvc = ret_lst[0] if isinstance(ret_lst, tuple) else ret_lst
            test_return_code(rvc)
            if type(ret_lst) == int:
                return None
            # return tuple only if there is more than one value to return
            ret_lst = ret_lst[1:] if type(ret_lst) == tuple else None
        # If only one value is in the list, give the value without items
        return ret_lst[0] if (type(ret_lst) == tuple and len(ret_lst) == 1) else ret_lst

    def _getListFcntApi(self,nameClass:str):
        # Récupérer tous les attributs de la classe
        leef = self.skinning
        leef = getattr(leef, nameClass)
        methodes = [m for m in dir(leef) if callable(getattr(leef, m)) and not m.startswith("__")]
        return  methodes


