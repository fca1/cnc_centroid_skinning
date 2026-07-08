from unittest import TestCase

from tests.support import make_api_or_skip


class TestMessageWindow(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.msg = make_api_or_skip().message_window

    def test_get_messages(self):
        self.msg.addMessage('tag string')
        lst1 = self.msg.getMessages()
        self.assertEqual(lst1[-1], 'tag string')
