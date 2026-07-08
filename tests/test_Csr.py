from unittest import TestCase

from cnc_centroid_skinning import WCS
from tests.support import make_api_or_skip


class TestCsr(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.csr = make_api_or_skip().csr

    def test_get_angle(self):
        self.csr.setAngle(12.3)
        self.assertEqual(self.csr.getAngle(WCS.WCS_1), 12.3)
