from .interface.ApiInterface import ApiInterface
from .cncenums import Coolant, SpindleDirection, ToolWearAdjustmentType


class Tinfo:
    def __init__(self, obj=None):
        self.coolant = None
        """Default coolant mode for this tool."""
        self.bin = None
        """Tool bin number."""
        self.diameter_offset = None
        """Cutter diameter compensation offset."""
        self.height_offset = None
        """Tool height offset."""
        self.d_number = None
        """Default diameter offset number."""
        self.spindle_speed = None
        """Default spindle speed."""
        self.spindle_direction = None
        """Default spindle direction."""
        if obj:
            self.coolant = obj.coolant
            self.bin = obj.bin
            self.diameter_offset = obj.diameter_offset
            self.height_offset = obj.height_offset
            self.d_number = obj.d_number
            self.spindle_speed = obj.spindle_speed
            self.spindle_direction = obj.spindle_direction


class Tool(ApiInterface):
    """Class to handle mill tool info."""

    def getToolLibrary(self) -> [Tinfo]:
        """Get tool info for all tools in the tool library."""

        answer = tuple(Tinfo(i) for i in self._call('GetToolLibrary'))
        assert len(answer) > 1
        return answer

    def getToolNumber(self) -> int:
        """Get the current tool number."""
        return self._call('GetToolNumber')

    def getCurrentHeightOffsetNumber(self) -> int:
        """Get the current height offset number."""
        return self._call('GetCurrentHeightOffsetNumber')

    def getToolInfo(self, t: int) -> Tinfo:
        info = self._call('GetToolInfo', t, wo_rc=True)
        """Get tool info for the specified tool number."""
        return Tinfo(info)

    def getHeightOffsetAmount(self, h: int = None) -> float:
        """Get the height offset amount."""
        if h is not None:
            return self._call('GetHeightOffsetAmount', h)
        else:
            return self._call('GetHeightOffsetAmount', )

    def getDiameterOffsetAmount(self) -> float:
        """Get the current diameter offset amount."""
        return self._call('GetDiameterOffsetAmount')

    def getToolSpindleSpeed(self, t: int = None) -> int:
        """Get spindle speed for the current or specified tool."""
        if t is not None:
            return self._call('GetToolSpindleSpeed', t)
        else:
            return self._call('GetToolSpindleSpeed', )

    def getCoolant(self, tool: int = None) -> Coolant:
        """Get coolant info for the current or specified tool."""
        if tool is not None:
            return self._call('GetCoolant', int(tool))
        else:
            return self._call('GetCoolant')

    def getToolSpindleDirection(self, tool: int = None) -> SpindleDirection:
        """Get spindle direction for the current or specified tool."""
        if tool is not None:
            return self._call('GetToolSpindleDirection', tool)
        else:
            return self._call('GetToolSpindleDirection')

    def getToolBin(self, tool: int = None) -> int:
        """Get bin number for the current or specified tool."""
        if tool is not None:
            return self._call('GetToolBin', tool)
        else:
            return self._call('GetToolBin')

    def setToolInfo(self, tool: int, tinfo: Tinfo):
        """Set tool info."""
        return self._call('SetToolInfo', tool, tinfo)

    def setBinNumber(self, tool: int, value: int):
        """Set the tool bin number."""
        return self._call('SetBinNumber', tool, value)

    def setCoolant(self, tool: int, aType: Coolant):
        """Set the coolant mode."""
        return self._call('SetCoolant', tool, aType)

    def setToolHeightOffsetAmount(self, tool: int, value: float):
        """Set the tool height offset amount."""
        return self._call('SetToolHeightOffsetAmount', tool, float(value))

    def setToolHeightOffsetAmout(self, tool: int, value: float):
        """Backward-compatible alias for the original misspelled method name."""
        return self.setToolHeightOffsetAmount(tool, value)

    def setSpindleDirection(self, tool: int, adir: SpindleDirection):
        """Set the tool spindle direction."""
        return self._call('SetSpindleDirection', tool, adir)

    def setSpindleSpeed(self, tool: int, speed: int):
        """Set the tool spindle speed."""
        return self._call('SetSpindleSpeed', tool, int(speed))

    def setToolDNumber(self, tool: int, dia: int):
        """Set the tool diameter number."""
        return self._call('SetToolDNumber', tool, int(dia))

    def setToolHNumber(self, tool: int, height: int):
        """Set the tool height number."""
        return self._call('SetToolHNumber', tool, int(height))

    def getToolHNumber(self, tool: int = None) -> int:
        """Get the H number for the current or specified tool."""
        if tool is None:
            return self._call('GetToolHNumber')
        else:
            return self._call('GetToolHNumber', tool)

    def getToolDNumber(self, tool: int = None) -> int:
        """Get the D number for the current or specified tool."""
        if tool is None:
            return self._call('GetToolDNumber')
        else:
            return self._call('GetToolDNumber', tool)

    def setWearAdjustment(self, tool: int, aType: ToolWearAdjustmentType, value: float):
        """Set the tool wear adjustment for a lathe tool."""
        return self._call('SetWearAdjustment', tool, aType, float(value))

    def getWearAdjustment(self, tool: int, aType: ToolWearAdjustmentType) -> float:
        """Get the tool wear adjustment for a lathe tool."""
        return self._call('GetWearAdjustment', tool, aType)
