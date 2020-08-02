from unittest import TestCase

from PyCncSkinning.PyCncSkinning.Skinning import Skinning


class TestMessageWindow(TestCase):
    assembly_path = r"C:\cnct"
    msg = Skinning(assembly_path).message_window

    def test_get_messages(self):
        self.msg.addMessage('tag string')
        lst1 = self.msg.getMessages()
        self.assertEqual(lst1[-1], 'tag string')
