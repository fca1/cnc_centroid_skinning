from unittest import TestCase

from PyCncSkinning.PyCncSkinning.Skinning import Skinning


class TestSys(TestCase):
    assembly_path = r"C:\cnct"
    sys = Skinning(assembly_path).system

    def test_get_system_identifier(self):
        self.sys.getSystemIdentifier()

    def test_exit_software(self):
        self.test_exit_software()

    def test_get_ether1616device_info(self):
        self.test_get_ether1616device_info()
