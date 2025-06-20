#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Api wrapper for cnc centroid API written is c#
    Name of dll has changed (V5.10 acorn)
"""

__version__ = "0.5.31"

import sys
from pathlib import Path

# load Python.NET
import clr
# noinspection PyUnresolvedReferences,PyPackageRequirements
from System import Array
# noinspection PyUnresolvedReferences,PyPackageRequirements
from System import String, Char, Int32, Double

# Verify conformity of platform (64 bits)
if sys.maxsize <= 2 ** 32:
    sys.stderr.write("Fatal : Python 32 bits détected")
    sys.exit(1)

# noinspection PyUnresolvedReferences
clr.AddReference('System.Collections')
# noinspection PyUnresolvedReferences,PyPackageRequirements
from System.Collections.Generic import Dictionary


# noinspection PyUnresolvedReferences
clr.AddReference("CentroidAPI")
# noinspection PyUnresolvedReferences
from CentroidAPI import CNCPipe as SCNCPipe

CNCPipe = SCNCPipe  # Main module of CNC CENTROID

from centroidAPI import detect_cnc, CentroidApi
from cncenums import *
from Tool import Tinfo


__all__ = [
           'CNCPipe', 'CentroidApi', 'DroCoordinates', 'ProbeBossOrientation', 'BitType', 'ForceState',
           'InversionState',
           'IOState', 'Rate', 'Direction',
           'IOMBit', 'ReturnCode', 'Viewport', 'CircularInterpolationPlane', 'CircularInterpolationDirection',
           'FeedHoldState',
           'MdiState', 'MoveMode', 'PositioningMode', 'UnitsOfMeasure', 'Value', 'HomingType', 'Ether1616Device',
           'Coolant', 'SpindleDirection', 'ToolWearAdjustmentType', 'Tinfo', 'WCS',
           'Axis', 'Csr', 'Dro', 'Job', 'MessageWindow', 'Parameter', 'Plc', 'Screen', 'State', 'Sys', 'Tool', 'Wcs',
            'UnlockVersions', 'MachineTypes',
           'detect_cnc']
