from unittest import TestCase

from PyCncSkinning.PyCncSkinning.Skinning import Skinning
from PyCncSkinning.PyCncSkinning.Wcs import WCS


class TestCsr(TestCase):
    assembly_path = r"C:\cnct"
    csr = Skinning(assembly_path).csr

    def test_get_angle(self):
        self.csr.setAngle(1.23, WCS.WCS_1)
        self.assertEqual(self.csr.getAngle(WCS.WCS_1), 1.23)
