r"""Regenerate cnc_centroid_skinning/cncenums.py from CentroidAPI.dll.

Usage:
    python tools/generate_cncenums.py C:\cncr
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


ENUM_SPECS = [
    ("Axes", "Axes"),
    ("Rate", "Axis.Rate"),
    ("WCS", "Wcs.WCS"),
    ("Direction", "Axis.Direction"),
    ("ReturnCode", "ReturnCode"),
    ("CircularInterpolationDirection", "State.CircularInterpolationDirection"),
    ("CircularInterpolationPlane", "State.CircularInterpolationPlane"),
    ("FeedHoldState", "State.FeedHoldState"),
    ("MdiState", "State.MdiState"),
    ("MoveMode", "State.MoveMode"),
    ("PositioningMode", "State.PositioningMode"),
    ("UnitsOfMeasure", "State.UnitsOfMeasure"),
    ("Value", "State.Value"),
    ("HomingType", "State.HomingType"),
    ("DroCoordinates", "Dro.DroCoordinates"),
    ("BitType", "Plc.BitType"),
    ("ForceState", "Plc.ForceState"),
    ("InversionState", "Plc.InversionState"),
    ("IOState", "Plc.IOState"),
    ("Viewport", "Screen.Viewport"),
    ("UnlockVersions", "Sys.UnlockVersions"),
    ("MachineTypes", "Sys.MachineTypes"),
    ("Coolant", "Tool.Coolant"),
    ("SpindleDirection", "Tool.SpindleDirection"),
    ("ToolWearAdjustmentType", "Tool.ToolWearAdjustmentType"),
    ("ProbeBossOrientation", "Job.ProbeBossOrientation"),
    ("CommunicationTypes", "InboundComm.CommunicationTypes"),
    ("JobInfoType", "InboundComm.JobInfoType"),
]

MEMBER_COMMENTS = {
    ("CommunicationTypes", "M2XX_MESSAGE_ACTIVE"): "CNC12 v5.42+ only.",
    ("CommunicationTypes", "M2XX_MESSAGE_CLEARED"): "CNC12 v5.42+ only.",
}

HEADER = '''r"""Generated CentroidAPI enum snapshot.

This file is intentionally importable without pythonnet or CentroidAPI.dll.
Regenerate it with:

    python tools/generate_cncenums.py C:\\cncr
"""

from enum import IntEnum


class _CentroidIntEnum(IntEnum):
    @classmethod
    def values(cls):
        return iter(cls)

'''

STRUCTS = '''

class IOMBit:
    def __init__(self, type=None, number=None, state=None, vcpButton=None):
        self.type = type
        self.number = number
        self.state = state
        self.vcpButton = vcpButton


class Ether1616Device:
    def __init__(self, IP=None, DeviceNumber=None):
        self.IP = IP
        self.DeviceNumber = DeviceNumber
'''


def resolve_member(root, dotted_path):
    current = root
    for part in dotted_path.split("."):
        current = getattr(current, part)
    return current


def render_enum(name, enum_type, enum_module):
    lines = [f"class {name}(_CentroidIntEnum):"]
    names = list(enum_module.GetNames(enum_type))
    if not names:
        lines.append("    pass")
    for member_name in names:
        value = int(enum_module.Parse(enum_type, member_name))
        comment = MEMBER_COMMENTS.get((name, member_name))
        suffix = f"  # {comment}" if comment else ""
        lines.append(f"    {member_name} = {value}{suffix}")
    return "\n".join(lines)


def generate(cnc12_path):
    from cnc_centroid_skinning.runtime import load_centroid_api

    CNCPipe = load_centroid_api(cnc12_path)

    from System import Enum

    sections = [HEADER.rstrip()]
    for public_name, dll_path in ENUM_SPECS:
        enum_type = resolve_member(CNCPipe, dll_path)
        sections.append(render_enum(public_name, enum_type, Enum))
    sections.append(STRUCTS.strip())
    return "\n\n\n".join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "cnc12_path",
        nargs="?",
        default=None,
        help="CNC12 directory containing CentroidAPI.dll, for example C:\\cncr",
    )
    parser.add_argument(
        "--output",
        default=Path(__file__).resolve().parents[1] / "cnc_centroid_skinning" / "cncenums.py",
        type=Path,
    )
    args = parser.parse_args()

    args.output.write_text(generate(args.cnc12_path), encoding="utf-8")
    print(f"generated {args.output}")


if __name__ == "__main__":
    main()
