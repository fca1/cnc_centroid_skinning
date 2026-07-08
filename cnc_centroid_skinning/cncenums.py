r"""Generated CentroidAPI enum snapshot.

This file is intentionally importable without pythonnet or CentroidAPI.dll.
Regenerate it with:

    python tools/generate_cncenums.py C:\cncr
"""

from enum import IntEnum


class _CentroidIntEnum(IntEnum):
    @classmethod
    def values(cls):
        return iter(cls)


class Axes(_CentroidIntEnum):
    AXIS_1 = 0
    AXIS_2 = 1
    AXIS_3 = 2
    AXIS_4 = 3
    AXIS_5 = 4
    AXIS_6 = 5
    AXIS_7 = 6
    AXIS_8 = 7


class Rate(_CentroidIntEnum):
    MAX = 0
    SLOW_JOG = 1
    FAST_JOG = 2
    FAST_JOG_MINUS = 3
    FAST_JOG_PLUS = 4
    FAST_JOG_PLUS_PROBE = 5
    FAST_JOG_MINUS_PROBE = 6
    SLOW_JOG_PROBE = 7
    HOME_JOG = 8


class WCS(_CentroidIntEnum):
    WCS_1 = 0
    WCS_2 = 1
    WCS_3 = 2
    WCS_4 = 3
    WCS_5 = 4
    WCS_6 = 5
    WCS_7 = 6
    WCS_8 = 7
    WCS_9 = 8
    WCS_10 = 9
    WCS_11 = 10
    WCS_12 = 11
    WCS_13 = 12
    WCS_14 = 13
    WCS_15 = 14
    WCS_16 = 15
    WCS_17 = 16
    WCS_18 = 17
    WCS_UNKNOWN = 18


class Direction(_CentroidIntEnum):
    PLUS = 0
    MINUS = 1


class ReturnCode(_CentroidIntEnum):
    ERROR_CLIENT_LOCKED = 0
    ERROR_INVALID_ARGUMENT = 1
    ERROR_INVALID_AXIS = 2
    ERROR_INVALID_PLC_BIT_NUMBER = 3
    ERROR_INVALID_PLC_BIT_TYPE = 4
    ERROR_INVALID_REQUEST = 5
    ERROR_INVALID_SKINNING_DATA_WORD_INDEX = 6
    ERROR_JOB_IN_PROGRESS = 7
    ERROR_PIPE_IS_BROKEN = 8
    ERROR_PLC_SEND_SKINNING_DATA = 9
    ERROR_SAVE_CONFIGURATION = 10
    ERROR_SEND_COMMAND = 11
    ERROR_SEND_PID_SETUPS = 12
    ERROR_SEND_SETUPS = 13
    ERROR_OUT_OF_RANGE = 14
    ERROR_CONVERSION = 15
    ERROR_UNKNOWN = 16
    ERROR_VALIDATION = 17
    STATUS_UNKNOWN = 18
    ERROR_DEPRECATED = 19
    ERROR_LICENSE_GENERAL_FAILURE = 20
    ERROR_LICENSE_MISMATCHED_VERSIONS = 21
    ERROR_LICENSE_MISMATCHED_SERIAL_NUMBER = 22
    ERROR_LICENSE_LOCKED = 23
    ERROR_INVALID_RETURN = 24
    ERROR_EXPERIMENTAL_FEATURE = 25
    ERROR_NOT_HOMED = 26
    ERROR_REPORT_PATH_EMPTY = 27
    ERROR_REPORT_PATH_INVALID = 28
    ERROR_REPORT_PATH_NOT_FOUND = 29
    SUCCESS = 30


class CircularInterpolationDirection(_CentroidIntEnum):
    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1


class CircularInterpolationPlane(_CentroidIntEnum):
    XY = 0
    ZX = 1
    YZ = 2


class FeedHoldState(_CentroidIntEnum):
    FEED_HOLD_ON = 0
    FEED_HOLD_OFF = 1
    UNKNOWN = 2


class MdiState(_CentroidIntEnum):
    IN_MDI = 0
    NOT_IN_MDI = 1
    UNKNOWN = 2


class MoveMode(_CentroidIntEnum):
    RAPID = 0
    LINEAR = 1
    CW_ARC = 2
    CCW_ARC = 3
    UNKNOWN = 4


class PositioningMode(_CentroidIntEnum):
    ABSOLUTE = 0
    INCREMENTAL = 1
    UNKNOWN = 2


class UnitsOfMeasure(_CentroidIntEnum):
    INCH_UNITS = 0
    METRIC_UNITS = 1
    UNKNOWN = 2


class Value(_CentroidIntEnum):
    MAX = 0
    MIN = 1


class HomingType(_CentroidIntEnum):
    JOG = 0
    HOMESWITCH = 1
    REFMARKHS = 2
    HOMEINPLACE = 3
    ABSOLUTEHOME = 4
    UNKNOWN = 5


class DroCoordinates(_CentroidIntEnum):
    DRO_LOCAL = 0
    DRO_MACHINE = 1
    DRO_DISTANCE_TO_GO = 2


class BitType(_CentroidIntEnum):
    Input = 0
    Output = 1
    Memory = 2
    UsbInput = 3


class ForceState(_CentroidIntEnum):
    NotForced = 0
    ForcedOn = 1
    ForcedOff = 2


class InversionState(_CentroidIntEnum):
    NotInverted = 0
    Inverted = 1


class IOState(_CentroidIntEnum):
    IO_LOGICAL_0 = 0
    IO_LOGICAL_1 = 1
    IO_INDEX_OUT_OF_RANGE = 2
    IO_STATE_UNKNOWN = 3


class Viewport(_CentroidIntEnum):
    VIEWPORT_ACTIVE_G_CODES = 0
    VIEWPORT_DRO = 1
    VIEWPORT_FKEY = 2
    VIEWPORT_MESSAGE = 3


class UnlockVersions(_CentroidIntEnum):
    UNKNOWN = 0
    FREE_MILL = 1
    PRO_MILL = 2
    ULTIMATE_MILL = 3
    ULTIMATE_PLUS_MILL = 4
    FREE_LATHE = 5
    PRO_LATHE = 6
    ULTIMATE_LATHE = 7
    ULTIMATE_PLUS_LATHE = 8
    FREE_ROUTER = 9
    PRO_ROUTER = 10
    ULTIMATE_ROUTER = 11
    ULTIMATE_PLUS_ROUTER = 12
    FREE_PLASMA = 13
    PRO_PLASMA = 14
    ULTIMATE_PLASMA = 15
    ULTIMATE_PLUS_PLASMA = 16
    FREE_LASER = 17
    PRO_LASER = 18
    ULTIMATE_LASER = 19
    ULTIMATE_PLUS_LASER = 20


class MachineTypes(_CentroidIntEnum):
    ACORN = 0
    ACORNSIX = 1
    HICKORY = 2
    OAK = 3
    ALLINONEDC = 4
    EMULATOR = 5
    UNKNOWN = 6


class Coolant(_CentroidIntEnum):
    OFF = 0
    MIST = 1
    FLOOD = 2
    UNKNOWN = 3


class SpindleDirection(_CentroidIntEnum):
    OFF = 0
    CW = 1
    CCW = 2
    UNKNOWN = 3


class ToolWearAdjustmentType(_CentroidIntEnum):
    TOOL_WEAR_ADJUSTMENT_X = 0
    TOOL_WEAR_ADJUSTMENT_Z = 1


class ProbeBossOrientation(_CentroidIntEnum):
    X_PLUS = 0
    Y_PLUS = 1
    X_MINUS = 2
    Y_MINUS = 3


class CommunicationTypes(_CentroidIntEnum):
    DRO_UPDATE = 0
    CNC12_SHUT_DOWN = 1
    PC_SHUT_DOWN = 2
    MESSAGE_WINDOW_MESSAGE = 3
    JOB_INFO = 4
    KEEP_PIPE_ALIVE = 5
    JOB_CONCLUDED = 6
    M2XX_MESSAGE_ACTIVE = 7
    M2XX_MESSAGE_CLEARED = 8


class JobInfoType(_CentroidIntEnum):
    CURRENT_LEVEL = 0
    TOP_LEVEL = 1


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
