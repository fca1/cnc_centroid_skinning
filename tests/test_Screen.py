from unittest import TestCase

from centroidAPI import CentroidAPI
from enums import Viewport
from cnc_centroid_skinning import PATH_CNC12



class TestScreen(TestCase):
    assembly_path = PATH_CNC12
    screen = CentroidAPI(assembly_path).screen

    def test_get_viewport_info(self):
        self.screen.getViewportInfo(Viewport.VIEWPORT_MESSAGE)
