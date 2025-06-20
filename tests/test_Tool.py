from unittest import TestCase

from cnc_centroid_skinning import PATH_CNC12, Tinfo
from centroidAPI import CentroidApi
from cncenums import ToolWearAdjustmentType, SpindleDirection, Coolant


class TestTool(TestCase):
    assembly_path = PATH_CNC12
    api = CentroidApi(assembly_path)
    tool = api.tool
    pass

    def test_get_tool_library(self):
        answer = self.tool.getToolLibrary()
        assert isinstance(answer, list)



    def test_get_tool_number(self):
        self.tool.getToolNumber()

    def test_get_current_height_offset_number(self):
        self.tool.getCurrentHeightOffsetNumber()

    def test_get_tool_info(self):
        info = self.tool.getToolInfo(1)
        assert isinstance(info, Tinfo)
        pass

    def test_get_height_offset_amount(self):
        self.tool.getHeightOffsetAmount()

    def test_get_diameter_offset_amount(self):
        self.tool.getDiameterOffsetAmount()

    def test_get_tool_spindle_speed(self):
        self.tool.getToolSpindleSpeed()

    def test_get_coolant(self):
        self.tool.getCoolant()

    def test_get_tool_spindle_direction(self):
        self.tool.getToolSpindleDirection()

    def test_get_tool_bin(self):
        self.tool.getToolBin()

    def test_get_tool_hnumber(self):
        self.tool.getToolHNumber()

    def test_get_tool_dnumber(self):
        self.tool.getToolDNumber()

    def test_get_wear_adjustment(self):
        self.tool.getWearAdjustment(1,ToolWearAdjustmentType.TOOL_WEAR_ADJUSTMENT_Z )

    def test_set_tool_info(self):
        self.tool.setToolInfo()

    def test_set_bin_number(self):
        self.tool.setBinNumber(0,0)

    def test_set_coolant(self):
        self.tool.setCoolant(1,Coolant.OFF)

    def test_set_tool_height_offset_amout(self):
        self.tool.setToolHeightOffsetAmout(0,5)

    def test_set_spindle_direction(self):
        self.tool.setSpindleDirection(0,SpindleDirection.OFF )

    def test_set_spindle_speed(self):
        self.tool.setSpindleSpeed(0,800)

    def test_set_tool_dnumber(self):
        self.tool.setToolDNumber(0,12)

    def test_set_tool_hnumber(self):
        self.tool.setToolHNumber(0,5)

    def test_set_wear_adjustment(self):
        self.tool.setWearAdjustment(0,ToolWearAdjustmentType.TOOL_WEAR_ADJUSTMENT_Z,1.2)

