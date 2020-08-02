from unittest import TestCase

from PyCncSkinning.PyCncSkinning.Screen import Viewport
from PyCncSkinning.PyCncSkinning.Skinning import Skinning


class TestScreen(TestCase):
    assembly_path = r"C:\cnct"
    screen = Skinning(assembly_path).screen

    def test_get_viewport_info(self):
        self.screen.getViewportInfo(Viewport.VIEWPORT_MESSAGE)
