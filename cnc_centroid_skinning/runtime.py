import os
import sys
from pathlib import Path


DEFAULT_CNC12_PATHS = (
    r"C:\cncm",
    r"C:\cnct",
    r"C:\cncr",
    r"C:\cncp",
    r"C:\Centroid_Mill_Intercon_Offline",
    r"C:\Centroid_Lathe_Intercon_Offline",
)

PATH_CNC12 = os.environ.get("CENTROID_CNC12_PATH") or os.environ.get("CNC12_PATH") or next(
    (path for path in DEFAULT_CNC12_PATHS if Path(path, "CentroidAPI.dll").exists()),
    DEFAULT_CNC12_PATHS[0],
)

_CNCPipe = None
_loaded_from = None
_dll_directories = []


def _candidate_directories(path_running=None):
    if path_running:
        yield Path(path_running)
    env_path = os.environ.get("CENTROID_CNC12_PATH") or os.environ.get("CNC12_PATH")
    if env_path:
        yield Path(env_path)
    for path in DEFAULT_CNC12_PATHS:
        yield Path(path)


def load_centroid_api(path_running=None):
    """Load CentroidAPI.dll with pythonnet and return CentroidAPI.CNCPipe."""
    global _CNCPipe, _loaded_from
    if _CNCPipe is not None:
        return _CNCPipe

    if sys.maxsize <= 2**32:
        raise RuntimeError("Python 64-bit is required to load CentroidAPI.dll.")

    try:
        import clr
    except ImportError as exc:
        raise RuntimeError("pythonnet is required to load CentroidAPI.dll.") from exc

    searched = []
    for directory in _candidate_directories(path_running):
        dll_path = directory / "CentroidAPI.dll"
        searched.append(str(dll_path))
        if not dll_path.exists():
            continue

        directory_str = str(directory)
        if directory_str not in sys.path:
            sys.path.insert(0, directory_str)
        if hasattr(os, "add_dll_directory"):
            _dll_directories.append(os.add_dll_directory(directory_str))
        clr.AddReference(str(dll_path))
        from CentroidAPI import CNCPipe

        _CNCPipe = CNCPipe
        _loaded_from = str(dll_path)
        return _CNCPipe

    try:
        clr.AddReference("CentroidAPI")
        from CentroidAPI import CNCPipe

        _CNCPipe = CNCPipe
        _loaded_from = "CentroidAPI"
        return _CNCPipe
    except Exception as exc:
        searched_text = "\n  - ".join(searched)
        raise RuntimeError(
            "Unable to load CentroidAPI.dll. Pass the CNC12 install directory to "
            "CentroidApi(path_running), set CENTROID_CNC12_PATH, or install CNC12 "
            f"in a standard directory. Searched:\n  - {searched_text}"
        ) from exc


def get_loaded_centroid_api_path():
    return _loaded_from
