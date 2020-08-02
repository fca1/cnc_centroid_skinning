from unittest import TestCase

from PyCncSkinning.PyCncSkinning.Skinning import Skinning


class TestSkinning(TestCase):
    assembly_path = r"C:\cnct"
    ct = Skinning(assembly_path)
    pass


class TestSkinning(TestCase):
    def test_is_constructed(self):
        self.assertTrue(TestSkinning.ct.test_is_constructed())
