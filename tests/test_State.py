from unittest import TestCase

from centroidAPI import CentroidAPI
from cnc_centroid_skinning import PATH_CNC12
from enums import Value


class TestState(TestCase):
    assembly_path = PATH_CNC12
    sta = CentroidAPI(assembly_path).state

    def test_get_screen_size(self):
        _x, _y = self.sta.getScreenSize()

    def test_get_monitor_size(self):
        _x, _y = self.sta.getMonitorSize()

    def test_get_screen_position(self):
        _x, _y = self.sta.getScreenPosition()

    def test_get_acorn_board_revision(self):
        _revision = self.sta.getAcornBoardRevision()

    def test_get_active_gcodes(self):
        _lst_actives = self.sta.getActiveGCodes()

    def test_get_feed_hold_state(self):
        self.sta.getFeedHoldState()

    def test_get_gcode_display(self):
        self.sta.getGCodeDisplay()

    def test_get_job_name_current(self):
        self.sta.getJobNameCurrent()

    def test_get_mdi_state(self):
        self.sta.getMdiState()

    def test_get_move_mode(self):
        self.sta.getMoveMode()

    def test_get_positioning_mode(self):
        self.sta.getPositioningMode()

    def test_get_units_of_measure_default(self):
        self.sta.getUnitsOfMeasureDefault()

    def test_get_units_of_measure_dro(self):
        self.sta.getUnitsOfMeasureDro()

    def test_get_feedrate(self):
        self.sta.getFeedrate()

    def test_get_spindle_speed(self):
        self.sta.getSpindleSpeed()

    def test_get_current_machine_position(self):
        self.sta.getCurrentMachinePosition()

    def test_get_feedrate_override(self):
        self.sta.getFeedrateOverride()

    def test_get_current_local_position(self):
        self.sta.getCurrentLocalPosition()

    def test_get_high_range_spindle_speed(self):
        self.sta.getHighRangeSpindleSpeed(Value.MIN)

    def test_get_machine_home_at_power_up(self):
        self.sta.getMachineHomeAtPowerUp()
