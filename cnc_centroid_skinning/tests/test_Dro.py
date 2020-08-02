from unittest import TestCase

from PyCncSkinning.PyCncSkinning.Dro import DroCoordinates
from PyCncSkinning.PyCncSkinning.Skinning import Skinning


class TestDro(TestCase):
    assembly_path = r"C:\cnct"
    dro = Skinning(assembly_path).dro

    def test_get_dro(self):
        self.dro.getDro(DroCoordinates.DRO_LOCAL)
        self.dro.setDroCoordinates(DroCoordinates.DRO_MACHINE)
