from typing import Tuple

# load Python.NET
# noinspection PyUnresolvedReferences
from System import Array
# noinspection PyUnresolvedReferences
from System import String, Char, Int32, Double, Decimal, Int64



class ApiInterface:
    def __init__(self, skinning, instance_name: str):
        self._skinning = skinning
        self._root_leef = instance_name
        pass

    def _call(self, *args, **kwargs) -> [Tuple, None]:
        from cncenums import ReturnCode
        from exceptions.SkinningException import ReturnCodeException
        def test_return_code(_rvc):
            rc = ReturnCode(int(_rvc))
            if rc != ReturnCode.SUCCESS:
                raise ReturnCodeException(f"Return Code returned by {fcnt}:={str(rc)}", rc)
            pass

        fcnt, *params = args
        fcnt = self._root_leef + "." + fcnt if self._root_leef else fcnt  # The root leef is same for object
        leef = self._skinning
        for obj in fcnt.split("."):
            leef = getattr(leef, obj)
            assert leef is not None
        # Transform float with Double  ( python float -> .net Double)
        params = [Double(i) if isinstance(i, float) else i for i in params]
        # Call the method found (pythonnet works between .net and python)
        ret_lst = leef(*params)
        if not kwargs.get('wo_rc', False):  # this option is used when return code is no waited
            # first item of list is a ReturnCode value. If No success, raise an Exception
            rvc = ret_lst[0] if isinstance(ret_lst, tuple) else ret_lst
            test_return_code(rvc)
            if type(ret_lst) == int:
                return None
            # return tuple only if there is more than one value to return
            ret_lst = ret_lst[1:] if type(ret_lst) == tuple else None
        # If only one value is in the list, give the value without items
        return ret_lst[0] if (type(ret_lst) == tuple and len(ret_lst) == 1) else ret_lst
