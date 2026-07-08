from typing import Tuple

# load Python.NET
# noinspection PyUnresolvedReferences
from System import Double



class ApiInterface:
    from .pythonnetAPIInterface import PythonnetAPIInterface
    def __init__(self, interface:PythonnetAPIInterface, instance_name: str):
        self._skinning = interface.skinning
        self._root_leef = instance_name
        self.path_running = interface.path_running
        pass

    @staticmethod
    def _normalize_result(value):
        if isinstance(value, tuple):
            return tuple(ApiInterface._normalize_result(item) for item in value)
        if isinstance(value, str):
            return value
        try:
            from System.Collections import IEnumerable
            if isinstance(value, IEnumerable):
                return list(value)
        except Exception:
            pass
        return value

    def _call(self, *args, **kwargs) -> [Tuple, None]:
        from ..cncenums import ReturnCode
        from ..exceptions.SkinningException import ReturnCodeException
        def test_return_code(_rvc):
            rc = ReturnCode(int(_rvc))
            if rc != ReturnCode.SUCCESS:
                raise ReturnCodeException(f"Return Code returned by {fcnt}:={str(rc)}", rc)
            pass

        if not args:
            raise TypeError("_call requires at least a method name")

        fcnt, *params = args
        fcnt = self._root_leef + "." + fcnt if self._root_leef else fcnt  # The root leef is same for object
        leef = self._skinning
        for obj in fcnt.split("."):
            try:
                leef = getattr(leef, obj)
            except AttributeError as exc:
                raise AttributeError(f"CentroidAPI object has no member '{fcnt}'") from exc
            if leef is None:
                raise AttributeError(f"CentroidAPI object member '{fcnt}' is None")
        # Transform float with Double  ( python float -> .net Double)
        params = [Double(i) if isinstance(i, float) else i for i in params]
        # Call the method found (pythonnet works between .net and python)
        ret_lst = leef(*params)
        ret_lst = self._normalize_result(ret_lst)
        if not kwargs.get('wo_rc', False):  # this option is used when return code is no waited
            # first item of list is a ReturnCode value. If No success, raise an Exception
            rvc = ret_lst[0] if isinstance(ret_lst, tuple) else ret_lst
            test_return_code(rvc)
            if isinstance(ret_lst, int):
                return None
            # return tuple only if there is more than one value to return
            ret_lst = ret_lst[1:] if isinstance(ret_lst, tuple) else None
        # If only one value is in the list, give the value without items
        return ret_lst[0] if (isinstance(ret_lst, tuple) and len(ret_lst) == 1) else ret_lst

    def __getattr__(self, name):
        """
        Fallback for CentroidAPI methods that are not wrapped yet.

        The Python API keeps the original convention where method names begin
        with a lower-case character.  CNC12 v5.x adds methods regularly; this
        fallback forwards unknown public calls to the .NET method with the first
        character upper-cased, preserving normal ReturnCode handling.
        """
        if name.startswith("_"):
            raise AttributeError(name)

        method_name = name[0].upper() + name[1:]

        def method(*args, **kwargs):
            return self._call(method_name, *args, **kwargs)

        return method
