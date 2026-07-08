from unittest import TestCase

from tests.support import make_api_or_skip


class TestSys(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sys = make_api_or_skip().sys

    def test_get_system_identifier(self):
        self.sys.getSystemIdentifier()

    def test_exit_software(self):
        # self.sys.exitSoftware()
        pass

    def test_get_ether1616device_info(self):
        self.sys.getEther1616DeviceInfo()

    def test_getMachineType(self):
        self.sys.getMachineType()
