from unittest import TestCase

from cnc_centroid_skinning import PATH_CNC12
from cnc_centroid_skinning.Dro import DroCoordinates
from centroidAPI import CentroidApi


class TestDro(TestCase):
    assembly_path = PATH_CNC12
    dro = CentroidApi(assembly_path).dro

    def test_get_dro(self):
        self.dro.getDro(DroCoordinates.DRO_LOCAL)
        self.dro.setDroCoordinates(DroCoordinates.DRO_MACHINE)
