from typing import List

from .interface.ApiInterface import ApiInterface


class MessageWindow(ApiInterface):
    """Class for status window information."""

    def getMessages(self) -> List[str]:
        """Get messages from the CNC12 message window."""
        return list(map(str, self._call('GetMessages')))

    def addMessage(self, message: str, backgroundColor: int = 0x800000, textColor: int = 0x00FFFF):
        """Display a message in the status window with the given colors."""
        return self._call('AddMessage', str(message), int(backgroundColor), int(textColor))

    @property
    def message(self):
        """Get the last message."""
        return self.getMessages()[-1]

    @message.setter
    def message(self, value):
        self.addMessage(value)
