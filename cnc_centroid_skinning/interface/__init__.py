#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Api wrapper for cnc centroid API written is c#
    Name of dll has changed (V5.10 acorn)
"""

__version__ = "0.0.5"



import sys
from pathlib import  Path

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



# refresh path of sys (for centroidAPI.dll's path)
sys.argv = *sys.argv,r"c:\\cncm"
if len(sys.argv) < 2:
    sys.stderr.write("please, give as parameter, the path of cncn/cnmt program (ex:c:\cncm)")
    sys.exit(1)
PATH_CNC12 = str(Path(sys.argv[1]))
sys.path.append(PATH_CNC12)


# noinspection PyUnresolvedReferences
clr.AddReference("CentroidAPI")
# noinspection PyUnresolvedReferences
from CentroidAPI import CNCPipe as SCNCPipe

CNCPipe = SCNCPipe              # Main module of CNC CENTROID


__all__ = [ 'CNCPipe', 'PythonnetAPI', 'DroCoordinates', 'ProbeBossOrientation', 'BitType', 'ForceState', 'InversionState',
           'IOState', 'Rate', 'Direction',
           'IOMBit', 'ReturnCode', 'Viewport', 'CircularInterpolationPlane', 'CircularInterpolationDirection',
           'FeedHoldState',
           'MdiState', 'MoveMode', 'PositioningMode', 'UnitsOfMeasure', 'Value', 'HomingType', 'Ether1616Device',
           'Coolant', 'SpindleDirection', 'ToolWearAdjustmentType', 'Tinfo', 'WCS',
           'Axis', 'Csr', 'Dro', 'Job', 'MessageWindow', 'Parameter', 'Plc', 'Screen', 'State', 'Sys', 'Tool', 'Wcs',
           'detect_cnc']



