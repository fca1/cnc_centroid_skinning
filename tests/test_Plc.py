from unittest import TestCase

from centroidAPI import CentroidAPI
from cnc_centroid_skinning import PATH_CNC12
from enums import IOMBit, BitType, ForceState, InversionState


class TestPLc(TestCase):
    assembly_path = PATH_CNC12
    plc = CentroidAPI(assembly_path).plc

    def test_get_watch_list(self):
        lst = [IOMBit()]
        # self.plc.SetWatchList(lst)
        self.plc.getWatchList(lst)

    def test_set_watch_list(self):
        pass

    def test_set_io_force_state(self):
        self.plc.setIoForceState(1, BitType.Input, ForceState.ForcedOff)

    def test_set_skinning_data_word(self):
        self.plc.setSkinningDataWord(1, 0, False)

    def test_get_skinning_data_word(self):
        self.plc.getSkinningDataWord(1)

    def test_set_input_iversion_state(self):
        self.plc.setInputIversionState(0, InversionState.Inverted)

    def test_set_input_force_state(self):
        self.plc.setInputIversionState(0, InversionState.NotIverted)

    def test_get_input_state(self):
        self.plc.getInputState(1)

    def test_get_output_state(self):
        self.plc.getOutputState(1)

    def test_get_memory_state(self):
        self.plc.getMemoryState(1)

    def test_get_word_value(self):
        self.plc.getWordValue(1)

    def test_get_double_word_value(self):
        self.plc.getDoubleWordValue(1)

    def test_get_float_word_value(self):
        self.plc.getFloatWordValue(1)

    def test_set_skin_event_state(self):
        self.plc.setSkinEventState(0, 0)

    def test_get_pc_system_variable_bit(self):
        self.plc.getPcSystemVariableBit(0)

    def test_get_plc_system_variable_bit(self):
        self.plc.getPlcSystemVariableBit(0)

    def test_get_vcp_led_states(self):
        self.plc.getVcpLedStates()
