#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Api wrapper for cnc centroid API written is c#
    Name of dll has changed (V5.24 acorn)
"""

__version__ = "1.0.0"

PATH_CNC12 = r"c:\cncm"

import sys

# load Python.NET
import clr
# noinspection PyUnresolvedReferences,PyPackageRequirements
from System import Array
# noinspection PyUnresolvedReferences,PyPackageRequirements
from System import String, Char, Int32, Double

if sys.maxsize <= 2 ** 32:
    sys.stderr.write("Fatal : Python 32 bits détected")
    sys.exit(1)

# noinspection PyUnresolvedReferences
clr.AddReference('System.Collections')
# noinspection PyUnresolvedReferences,PyPackageRequirements
from System.Collections.Generic import Dictionary

sys.path.append(PATH_CNC12)

# noinspection PyUnresolvedReferences
clr.AddReference("CentroidAPI")
# noinspection PyUnresolvedReferences
from CentroidAPI import CNCPipe as SCNCPipe

CNCPipe = SCNCPipe

"""
from Dro import DroCoordinates
from Job import ProbeBossOrientation
from Plc import BitType, ForceState, InversionState, IOState, IOMBit
from Screen import Viewport
from State import CircularInterpolationPlane, \
    CircularInterpolationDirection, FeedHoldState, MdiState, MoveMode, PositioningMode, UnitsOfMeasure, Value, \
    HomingType
from Sys import Ether1616Device
from Tool import Coolant, SpindleDirection, Tinfo
from Tool import ToolWearAdjustmentaType
from Wcs import WCS
from centroidAPI import detect_cnc, CentroidAPI


__all__ = [ 'CNCPipe','CentroidAPI', 'DroCoordinates', 'ProbeBossOrientation', 'BitType', 'ForceState', 'InversionState',
           'IOState', 'Rate', 'Direction', 'CncPipe',
           'IOMBit', 'ReturnCode', 'Viewport', 'CircularInterpolationPlane', 'CircularInterpolationDirection',
           'FeedHoldState',
           'MdiState', 'MoveMode', 'PositioningMode', 'UnitsOfMeasure', 'Value', 'HomingType', 'Ether1616Device',
           'Coolant', 'SpindleDirection', 'ToolWearAdjustmentaType', 'Tinfo', 'WCS',
           'Axis', 'Csr', 'Dro', 'Job', 'MessageWindow', 'Parameter', 'Plc', 'Screen', 'State', 'Sys', 'Tool', 'Wcs',
           'detect_cnc','MachineTypes','UnlockVersions','MotorPower','ConsoleTypes']
"""
