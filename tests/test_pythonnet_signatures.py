import ast
import unittest
from pathlib import Path

from cnc_centroid_skinning import PATH_CNC12
from cnc_centroid_skinning import Axes, BitType, IOState, IOMBit
from cnc_centroid_skinning import CentroidApi
from cnc_centroid_skinning.runtime import load_centroid_api


WRAPPER_ROOTS = {
    "Axis.py": "axis",
    "Csr.py": "csr",
    "Dro.py": "dro",
    "InboundComm.py": "inbound_communications",
    "Job.py": "job",
    "MessageWindow.py": "message_window",
    "Parameter.py": "parameter",
    "Pipe.py": "",
    "Plc.py": "plc",
    "Screen.py": "screen",
    "State.py": "state",
    "Sys.py": "system",
    "Tool.py": "tool",
    "Wcs.py": "wcs",
}

DOTNET_TYPE_PATHS = {
    "axis": "Axis",
    "csr": "Csr",
    "dro": "Dro",
    "inbound_communications": "InboundComm",
    "job": "Job",
    "message_window": "MessageWindow",
    "parameter": "Parameter",
    "plc": "Plc",
    "screen": "Screen",
    "state": "State",
    "system": "Sys",
    "tool": "Tool",
    "wcs": "Wcs",
    "": "",
}


def _resolve(root, dotted_path):
    current = root
    for part in dotted_path.split("."):
        if part:
            current = getattr(current, part)
    return current


def _wrapper_calls():
    package_root = Path(__file__).resolve().parents[1] / "cnc_centroid_skinning"
    for file_name, root_name in WRAPPER_ROOTS.items():
        path = package_root / file_name
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "_call"
            ):
                continue
            if not node.args or not isinstance(node.args[0], ast.Constant):
                continue
            if not isinstance(node.args[0].value, str):
                continue
            yield file_name, node.lineno, root_name, node.args[0].value, len(node.args) - 1


class TestPythonnetSignatures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.CNCPipe = load_centroid_api(PATH_CNC12)
            import clr
            from System.Reflection import BindingFlags
        except Exception as exc:
            raise unittest.SkipTest(f"CentroidAPI.dll is not available: {exc}") from exc
        cls.clr = clr
        cls.binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static

    def _methods(self, dotnet_class):
        methods = {}
        for method in self.clr.GetClrType(dotnet_class).GetMethods(self.binding_flags):
            if method.IsSpecialName:
                continue
            params = method.GetParameters()
            methods.setdefault(method.Name, []).append(params)
        return methods

    def test_wrapped_methods_exist_with_pythonnet_argument_counts(self):
        missing = []
        bad_counts = []
        for file_name, line, root_name, method_name, arg_count in _wrapper_calls():
            dotnet_path = DOTNET_TYPE_PATHS[root_name]
            dotnet_class = self.CNCPipe if not dotnet_path else _resolve(self.CNCPipe, dotnet_path)
            overloads = self._methods(dotnet_class).get(method_name)
            if overloads is None:
                missing.append(f"{file_name}:{line} {root_name or 'CNCPipe'}.{method_name}")
                continue

            expected_counts = [sum(1 for param in params if not param.IsOut) for params in overloads]
            if arg_count not in expected_counts:
                bad_counts.append(
                    f"{file_name}:{line} {method_name} has {arg_count} args; expected one of {expected_counts}"
                )

        self.assertEqual([], missing)
        self.assertEqual([], bad_counts)

    def test_python_enums_are_coerced_to_dotnet_enums(self):
        api = CentroidApi(PATH_CNC12)
        axis = api.axis._coerce_param(Axes.AXIS_1)
        bit_type = api.plc._coerce_param(BitType.Output)
        iombit = api.plc._to_dotnet_iombit(
            IOMBit(type=BitType.Output, number=7, state=IOState.IO_LOGICAL_1, vcpButton=0)
        )

        self.assertEqual(self.CNCPipe.Axes, type(axis))
        self.assertEqual(self.CNCPipe.Plc.BitType, type(bit_type))
        self.assertEqual(self.CNCPipe.Plc.IOMBit, type(iombit))
        self.assertEqual(7, iombit.number)
