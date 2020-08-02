from unittest import TestCase

from PyCncSkinning.PyCncSkinning.Skinning import Skinning


class TestTool(TestCase):
    assembly_path = r"C:\cnct"
    tool = Skinning(assembly_path).tool
    pass

    def test_get_tool_number(self):
        self.tool.getToolNumber()

    def test_get_current_height_offset_number(self):
        self.tool.getCurrentHeightOffsetNumber()

    def test_get_tool_info(self):
        self.tool.getToolInfo()

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

    def test_set_tool_info(self):
        self.tool.setToolInfo()

    def test_set_bin_number(self):
        self.tool.setBinNumber()

    def test_set_coolant(self):
        self.tool.setCoolant()

    def test_set_tool_height_offset_amout(self):
        self.tool.setToolHeightOffsetAmout()

    def test_set_spindle_direction(self):
        self.tool.setSpindleDirection()

    def test_set_spindle_speed(self):
        self.tool.setSpindleSpeed()

    def test_set_tool_dnumber(self):
        self.tool.setToolDNumber()

    def test_set_tool_hnumber(self):
        self.tool.setToolHNumber()

    def test_get_tool_hnumber(self):
        self.tool.getToolHNumber()

    def test_get_tool_dnumber(self):
        self.tool.getToolDNumber()

    def test_set_wear_adjustment(self):
        self.tool.setWearAdjustment()

    def test_get_wear_adjustment(self):
        self.tool.getWearAdjustment()
