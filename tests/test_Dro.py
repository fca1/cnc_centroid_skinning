from unittest import TestCase

from cnc_centroid_skinning import DroCoordinates
from tests.support import make_api_or_skip


class TestDro(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dro = make_api_or_skip().dro

    def test_get_dro(self):
        self.dro.getDro(DroCoordinates.DRO_LOCAL)
        self.dro.setDroCoordinates(DroCoordinates.DRO_MACHINE)
