#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Api wrapper for cnc centroid API written in c#  (https://www.centroidcnc.com/)
"""

__version__ = "0.0.1"

from .Axis import Axes
from .Tool import ToolWearAdjustmentaType

from .Dro import DroCoordinates
from .Job import ProbeBossOrientation
from .Plc import BitType, ForceState, InversionState, IOState, IOMBit
from .Screen import Viewport
from .cncSkinning import detect_cnc, CncSkinning
from .State import CircularInterpolationPlane, \
    CircularInterpolationDirection, FeedHoldState, MdiState, MoveMode, PositioningMode, UnitsOfMeasure, Value, \
    HomingType
from .Sys import Ether1616Device
from .Tool import Coolant, SpindleDirection, Tinfo
from .Wcs import WCS
from .Axis import Direction,Rate


__all__ = ['CncSkinning', 'Axes', 'DroCoordinates', 'ProbeBossOrientation', 'BitType', 'ForceState', 'InversionState',
           'IOState','Rate','Direction',
           'IOMBit', 'ReturnCode', 'Viewport', 'CircularInterpolationPlane', 'CircularInterpolationDirection',
           'FeedHoldState',
           'MdiState', 'MoveMode', 'PositioningMode', 'UnitsOfMeasure', 'Value', 'HomingType', 'Ether1616Device',
           'Coolant', 'SpindleDirection', 'ToolWearAdjustmentaType', 'Tinfo', 'WCS',
           'Axis', 'Csr', 'Dro', 'Job', 'MessageWindow', 'Parameter', 'Plc', 'Screen', 'State', 'Sys', 'Tool', 'Wcs',
           'detect_cnc']

