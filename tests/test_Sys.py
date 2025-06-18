from unittest import TestCase

from cnc_centroid_skinning import PATH_CNC12
from centroidAPI import CentroidApi


class TestSys(TestCase):
    assembly_path = PATH_CNC12
    sys = CentroidApi(assembly_path).sys

    def test_get_system_identifier(self):
        self.sys.getSystemIdentifier()

    def test_exit_software(self):
        #self.sys.exitSoftware()
        pass

    def test_get_ether1616device_info(self):
        self.sys.getEther1616DeviceInfo()
