from unittest import TestCase

from cnc_centroid_skinning import PATH_CNC12
from centroidAPI import CentroidApi



class TestScreen(TestCase):
    assembly_path = PATH_CNC12
    screen = CentroidApi(assembly_path).screen

    def test_get_viewport_info(self):
        from cnc_centroid_skinning import Viewport
        self.screen.getViewportInfo(Viewport.VIEWPORT_MESSAGE)
