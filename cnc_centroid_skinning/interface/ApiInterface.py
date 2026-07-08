from typing import Tuple
from enum import IntEnum

# load Python.NET
# noinspection PyUnresolvedReferences
from System import Double


_DOTNET_ENUM_PATHS = {
    "Axes": "Axes",
    "Rate": "Axis.Rate",
    "WCS": "Wcs.WCS",
    "Direction": "Axis.Direction",
    "ReturnCode": "ReturnCode",
    "CircularInterpolationDirection": "State.CircularInterpolationDirection",
    "CircularInterpolationPlane": "State.CircularInterpolationPlane",
    "FeedHoldState": "State.FeedHoldState",
    "MdiState": "State.MdiState",
    "MoveMode": "State.MoveMode",
    "PositioningMode": "State.PositioningMode",
    "UnitsOfMeasure": "State.UnitsOfMeasure",
    "Value": "State.Value",
    "HomingType": "State.HomingType",
    "DroCoordinates": "Dro.DroCoordinates",
    "BitType": "Plc.BitType",
    "ForceState": "Plc.ForceState",
    "InversionState": "Plc.InversionState",
    "IOState": "Plc.IOState",
    "Viewport": "Screen.Viewport",
    "UnlockVersions": "Sys.UnlockVersions",
    "MachineTypes": "Sys.MachineTypes",
    "Coolant": "Tool.Coolant",
    "SpindleDirection": "Tool.SpindleDirection",
    "ToolWearAdjustmentType": "Tool.ToolWearAdjustmentType",
    "ProbeBossOrientation": "Job.ProbeBossOrientation",
    "CommunicationTypes": "InboundComm.CommunicationTypes",
    "JobInfoType": "InboundComm.JobInfoType",
}


class ApiInterface:
    from .pythonnetAPIInterface import PythonnetAPIInterface
    def __init__(self, interface:PythonnetAPIInterface, instance_name: str):
        self._interface = interface
        self._skinning = interface.skinning
        self._root_leef = instance_name
        self.path_running = interface.path_running
        pass

    def _dotnet_enum_type(self, enum_name):
        dotted_path = _DOTNET_ENUM_PATHS.get(enum_name)
        if dotted_path is None:
            return None
        current = self._interface.cls
        for part in dotted_path.split("."):
            current = getattr(current, part)
        return current

    def _coerce_param(self, value):
        if isinstance(value, IntEnum):
            enum_type = self._dotnet_enum_type(value.__class__.__name__)
            if enum_type is not None:
                from System import Enum

                return Enum.ToObject(enum_type, int(value))
        return Double(value) if isinstance(value, float) else value

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
        fcnt = self._root_leef + "." + fcnt if self._root_leef else fcnt  # Prefix with the CNCPipe child object.
        leef = self._skinning
        for obj in fcnt.split("."):
            try:
                leef = getattr(leef, obj)
            except AttributeError as exc:
                raise AttributeError(f"CentroidAPI object has no member '{fcnt}'") from exc
            if leef is None:
                raise AttributeError(f"CentroidAPI object member '{fcnt}' is None")
        # Transform float with Double  ( python float -> .net Double)
        params = [self._coerce_param(i) for i in params]
        # Call the method found (pythonnet works between .net and python)
        ret_lst = leef(*params)
        ret_lst = self._normalize_result(ret_lst)
        if not kwargs.get('wo_rc', False):  # Used when the API method does not return a ReturnCode.
            # First tuple item is a ReturnCode; raise on non-success.
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
