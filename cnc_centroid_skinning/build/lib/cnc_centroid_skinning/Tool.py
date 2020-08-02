from enum import IntEnum, unique

from .cncSkinningInterface import CncSkinningInterface


@unique
class Coolant(IntEnum):
    """This field specifies a default coolant aType to use with each tool. Possible values are FLOOD, MIST, or OFF. Intercon uses this information to automatically insert M7 or M8 after a tool change. """
    OFF = 0
    """Coolant off."""
    MIST = 1
    """Coolant mist."""
    FLOOD = 2
    """Coolant flood"""
    UNKNOWN = 3
    """Indicates an error determining the coolant aType."""


@unique
class SpindleDirection(IntEnum):
    """for the different spindle directions."""
    OFF = 0
    """Spindle off."""
    CW = 1
    """Spindle direction clockwise"""
    CCW = 2
    """Spindle direction counterclockwise"""
    UNKNOWN = 3
    """Indicates an error in determining the spindle direction"""


@unique
class ToolWearAdjustmentaType(IntEnum):
    """for tool wear adjustment."""
    X = 0
    Z = 1


class Tinfo:
    """Structure to hold tool library info """
    def __init__(self, obj=None):
        self.coolant = None
        """This field specifies a default coolant aType to use with each tool. Possible values are FLOOD, MIST, or OFF. Intercon uses this information to automatically insert M7 or M8 after a tool change. """
        self.bin = None
        """This field tells the bin number of tool. """
        self.diameter_offset = None
        """This field tells the control the distance to adjust when cutter diameter compensation (G41 or G42) is used with a particular D value. """
        self.height_offset = None
        """This field specifies a default Diameter (D) number to use with each tool. Possible values are 1 to 200. Intercon uses this information to provide a default D value at each tool change. """
        self.d_number = None
        """This field specifies a default Diameter (D) number to use with each tool. Possible values are 1 to 200. Intercon uses this information to provide a default D value at each tool change. """
        self.spindle_speed = None
        """This field specifies a default spindle speed to use with each tool. Possible values are 0 to 500000. Intercon uses this information to automatically insert an S code after a tool change. """
        self.spindle_direction = None
        """This field specifies a default spindle direction to use with each tool. Possible values are CW, CCW, or OFF. Intercon uses this information to automatically insert M3 or M4 after a tool change. """
        if obj:
            self.coolant = Coolant(obj.coolant)
            self.bin = obj.bin
            self.diameter_offset = obj.diameter_offset
            self.height_offset = obj.height_offset
            self.d_number = obj.d_number
            self.spindle_speed = obj.spindle_speed
            self.spindle_direction = SpindleDirection(obj.spindle_direction)


class Tool:
    """Class to handle Mill Tool Info"""
    def __init__(self, interface: CncSkinningInterface):
        self.interface = interface

    def getToolNumber(self) -> int:
        """:return: s the current tool number. """
        return self.interface('tool.GetToolNumber', 0)

    def getCurrentHeightOffsetNumber(self) -> int:
        """:return: s the current Height offset number. """
        return self.interface('tool.GetCurrentHeightOffsetNumber', 0)

    def getToolInfo(self, t: int = None) -> Tinfo:
        """:return: s tool info for the tool with specified tool number. """
        if t is not None:
            return Tinfo(self.interface('tool.GetToolInfo', t, wo_rc=True))
        else:
            return Tinfo(self.interface('tool.GetToolInfo', wo_rc=True))

    def getHeightOffsetAmount(self, h: int = None) -> float:
        """:return:  the height offset amount for the current H number. """
        if h is not None:
            return self.interface('tool.GetHeightOffsetAmount', h, 0.0)
        else:
            return self.interface('tool.GetHeightOffsetAmount', 0.0)

    def getDiameterOffsetAmount(self, d: int) -> float:
        """:return: s the diameter offset amount for the specified D number. """
        return self.interface('tool.GetDiameterOffsetAmount', d, 0.0)

    def getToolSpindleSpeed(self, t: int = None):
        """:return: s the spindle speed for the current tool or the specified tool number. """
        if t is not None:
            return self.interface('tool.GetToolSpindleSpeed', t, 0.0)
        else:
            return self.interface('tool.GetToolSpindleSpeed', 0.0)

    def getCoolant(self, coolant: Coolant, tool: int = None):
        """:return: s the coolant info for the specified tool. """
        if tool is not None:
            return self.interface('tool.GetCoolant', tool, coolant.value)
        else:
            return self.interface('tool.GetCoolant', coolant.value)

    def getToolSpindleDirection(self, tool: int = None) -> SpindleDirection:
        """:return: s the spindle direction for the current tool. """
        if tool is not None:
            return SpindleDirection(self.interface('tool.GetToolSpindleDirection', tool))
        else:
            return SpindleDirection(self.interface('tool.GetToolSpindleDirection'))

    def getToolBin(self, tool: int = None) -> int:
        """:return: s the bin number for the specified tool. """
        if tool is not None:
            return self.interface('tool.GetToolBin', tool, 0)
        else:
            return self.interface('tool.GetToolBin', 0)

    def setToolInfo(self, tool: int, tinfo: Tinfo):
        """Specifies the information for tool """
        return self.interface('tool.SetToolInfo', tool, tinfo)

    def setBinNumber(self, tool: int, value: int):
        """Specifies the information for tool """
        return self.interface('tool.SetBinNumber', tool, value)

    def setCoolant(self, tool: int, aType: Coolant):
        """Set the coolant method """
        return self.interface('tool.SetCoolant', tool, aType.value)

    def setToolHeightOffsetAmout(self, tool: int, value: float):
        """Set the tool diameter offset Amount """
        return self.interface('tool.SetToolHeightOffsetAmout', tool, float(value))

    def setSpindleDirection(self, tool: int, dir: SpindleDirection):
        """Set the tool spindle direction """
        return self.interface('tool.SetSpindleDirection', tool, dir.value)

    def setSpindleSpeed(self, tool: int, speed: int):
        """Set the tool spindle speed """
        return self.interface('tool.SetSpindleSpeed', tool, int(speed))

    def setToolDNumber(self, tool: int, dia: int):
        """Set the Tool Diameter Number """
        return self.interface('tool.SetToolDNumber', tool, int(dia))

    def setToolHNumber(self, tool: int, height: int):
        """Set the Tool Height Number """
        return self.interface('tool.SetToolHNumber', tool, int(height))

    def getToolHNumber(self, tool: int = None) -> int:
        """:return: s the H number for the active tool. """
        if tool is None:
            return self.interface('tool.GetToolHNumber', 0)
        else:
            return self.interface('tool.GetToolHNumber', tool, 0)

    def getToolDNumber(self, tool: int = None) -> int:
        """:return: s the D number for the active tool. """
        if tool is None:
            return self.interface('tool.GetToolDNumber', 0)
        else:
            return self.interface('tool.GetToolDNumber', tool, 0)

    def setWearAdjustment(self, tool: int, aType: ToolWearAdjustmentaType, value: float):
        """Set the tool wear adjustment for a lathe tool. """
        return self.interface('tool.SetWearAdjustment', tool, aType.value, float(value))

    def getWearAdjustment(self, tool: int, aType: ToolWearAdjustmentaType) -> float:
        """:return:  the tool wear adjustment for a lathe tool. """
        return self.interface('tool.GetWearAdjustment', tool, aType.value)
