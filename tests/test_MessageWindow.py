from unittest import TestCase

from cnc_centroid_skinning import PATH_CNC12
from centroidAPI import CentroidApi


class TestMessageWindow(TestCase):
    assembly_path = PATH_CNC12
    msg = CentroidApi(assembly_path).message_window

    def test_get_messages(self):
        self.msg.addMessage('tag string')
        lst1 = self.msg.getMessages()
        self.assertEqual(lst1[-1], 'tag string')
