


from cncenums import Coolant, SpindleDirection, ToolWearAdjustmentType
from centroidAPIInterface import CentroidAPIInterface



class Tinfo:
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
            self.coolant = obj.coolant
            self.bin = obj.bin
            self.diameter_offset = obj.diameter_offset
            self.height_offset = obj.height_offset
            self.d_number = obj.d_number
            self.spindle_speed = obj.spindle_speed
            self.spindle_direction = obj.spindle_direction




class Tool:
    """Class to handle Mill Tool Info"""

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    def getToolLibrary(self):
        return self.interface('tool.GetToolLibrary')

    def getToolNumber(self) -> int:
        """:return: s the current tool number. """
        return self.interface('tool.GetToolNumber')

    def getCurrentHeightOffsetNumber(self) -> int:
        """:return: s the current Height offset number. """
        return self.interface('tool.GetCurrentHeightOffsetNumber')

    def getToolInfo(self, t: int) -> Tinfo:
        info = self.interface('tool.GetToolInfo', t, wo_rc=True)
        """:return: s tool info for the tool with specified tool number. """
        return Tinfo(info)

    def getHeightOffsetAmount(self, h: int = None) -> float:
        """:return:  the height offset amount for the current H number. """
        if h is not None:
            return self.interface('tool.GetHeightOffsetAmount', h)
        else:
            return self.interface('tool.GetHeightOffsetAmount', )

    def getDiameterOffsetAmount(self) -> float:
        """:return: s the diameter offset amount for the specified D number. """
        return self.interface('tool.GetDiameterOffsetAmount')

    def getToolSpindleSpeed(self, t: int = None) ->int:
        """:return: s the spindle speed for the current tool or the specified tool number. """
        if t is not None:
            return self.interface('tool.GetToolSpindleSpeed', t )
        else:
            return self.interface('tool.GetToolSpindleSpeed', )

    def getCoolant(self, tool: int = None) -> Coolant:
        """:return: s the coolant info for the specified tool. """
        if tool is not None:
            return self.interface('tool.GetCoolant',int(tool))
        else:
            return self.interface('tool.GetCoolant')

    def getToolSpindleDirection(self, tool: int = None) -> SpindleDirection:
        """:return: s the spindle direction for the current tool. """
        if tool is not None:
            return self.interface('tool.GetToolSpindleDirection', tool)
        else:
            return self.interface('tool.GetToolSpindleDirection')

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
        return self.interface('tool.SetCoolant', tool, aType)

    def setToolHeightOffsetAmout(self, tool: int, value: float):
        """Set the tool diameter offset Amount """
        return self.interface('tool.SetToolHeightOffsetAmout', tool, float(value))

    def setSpindleDirection(self, tool: int, adir: SpindleDirection):
        """Set the tool spindle direction """
        return self.interface('tool.SetSpindleDirection', tool, adir)

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

    def setWearAdjustment(self, tool: int, aType: ToolWearAdjustmentType, value: float):
        """Set the tool wear adjustment for a lathe tool. """
        return self.interface('tool.SetWearAdjustment', tool, aType, float(value))

    def getWearAdjustment(self, tool: int, aType: ToolWearAdjustmentType) -> float:
        """:return:  the tool wear adjustment for a lathe tool. """
        return self.interface('tool.GetWearAdjustment', tool, aType)
