from unittest import TestCase

from cnc_centroid_skinning import PATH_CNC12
from cnc_centroid_skinning.centroidAPI import CentroidAPI
from enums import WCS


class TestCsr(TestCase):
    assembly_path = PATH_CNC12
    csr = CentroidAPI(assembly_path).csr

    def test_get_angle(self):
        self.csr.setAngle(1.23, WCS.WCS_1)
        self.assertEqual(self.csr.getAngle(WCS.WCS_1), 1.23)