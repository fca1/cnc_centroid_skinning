#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python wrapper for the Centroid CNC12 CentroidAPI.dll."""

__version__ = "0.5.42"

from .runtime import PATH_CNC12, get_loaded_centroid_api_path, load_centroid_api
from .centroidAPI import CentroidApi, detect_cnc

_ENUM_NAMES = {
    "Axes",
    "BitType",
    "CircularInterpolationDirection",
    "CircularInterpolationPlane",
    "CommunicationTypes",
    "Coolant",
    "Direction",
    "DroCoordinates",
    "Ether1616Device",
    "FeedHoldState",
    "ForceState",
    "HomingType",
    "IOMBit",
    "IOState",
    "InversionState",
    "JobInfoType",
    "MachineTypes",
    "MdiState",
    "MoveMode",
    "PositioningMode",
    "ProbeBossOrientation",
    "Rate",
    "ReturnCode",
    "SpindleDirection",
    "ToolWearAdjustmentType",
    "UnitsOfMeasure",
    "UnlockVersions",
    "Value",
    "Viewport",
    "WCS",
}


def __getattr__(name):
    if name == "CNCPipe":
        return load_centroid_api()
    if name == "Tinfo":
        from .Tool import Tinfo

        return Tinfo
    if name in _ENUM_NAMES:
        from . import cncenums

        return getattr(cncenums, name)
    raise AttributeError(name)


__all__ = [
    "CNCPipe",
    "CentroidApi",
    "PATH_CNC12",
    "detect_cnc",
    "get_loaded_centroid_api_path",
    "load_centroid_api",
    "Tinfo",
    *_ENUM_NAMES,
]
