from unittest import TestCase

from tests.support import make_api_or_skip



class TestScreen(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.screen = make_api_or_skip().screen

    def test_get_viewport_info(self):
        from cnc_centroid_skinning import Viewport
        self.screen.getViewportInfo(Viewport.VIEWPORT_MESSAGE)
