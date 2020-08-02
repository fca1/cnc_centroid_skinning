from typing import List

from .cncSkinningInterface import CncSkinningInterface


class MessageWindow:
    """Class for getting status window information"""

    def __init__(self, interface: CncSkinningInterface):
        self.interface = interface

    def getMessages(self) -> List[str]:
        """:return: the messages from the Message Window in CNC12."""
        return list(map(str, self.interface('message_window.GetMessages', [])))

    def addMessage(self, message: str, backgroundColor: int = 0x800000, textColor: int = 0x00FFFF):

        """
        Displays a message in the status window with the given colors.
        .. warning:: message is correctly written but colors don't change.
        """

        return self.interface('message_window.AddMessage', str(message), int(backgroundColor), int(textColor))

    @property
    def message(self):
        """
        :return: The last message displayed in window message.
        """
        return self.getMessages()[-1]

    @message.setter
    def message(self, value):
        self.addMessage(value)
