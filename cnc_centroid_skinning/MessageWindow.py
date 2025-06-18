from typing import List

from interface.ApiInterface import ApiInterface


class MessageWindow(ApiInterface):
    """Class for getting status window information"""


    def getMessages(self) -> List[str]:
        """:return: the messages from the Message Window in CNC12."""
        return list(map(str, self._call('message_window.GetMessages', [])))

    def addMessage(self, message: str, backgroundColor: int = 0x800000, textColor: int = 0x00FFFF):
        """Displays a message in the status window with the given colors. """
        return self._call('message_window.AddMessage', str(message), int(backgroundColor), int(textColor))

    @property
    def message(self):
        """

        :return: The last message
        """
        return self.getMessages()[-1]

    @message.setter
    def message(self, value):
        self.addMessage(value)
