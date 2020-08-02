from dataclasses import dataclass

import typing

from .cncSkinningInterface import CncSkinningInterface
# noinspection PyUnresolvedReferences
from System.Collections.Generic import List

from .exceptions.SkinningException import ReturnCodeException


@dataclass
class Ether1616Device:
    ip: str
    DeviceNumber: int


class Sys:
    """A class for getting system-related information """
    def __init__(self, interface: CncSkinningInterface):
        self.interface = interface

    def getSystemIdentifier(self) -> int:

        """
        :return: Get the System ID of the machine to which this skinning app is connected. """
        return self.interface('system.GetSystemIdentifier', 0)

    def exitSoftware(self):
        """Closes CNCXX software gracefully. """
        return self.interface('system.ExitSoftware')

    # @TODO a card is needed to test this method, not yet verified
    def getEther1616DeviceInfo(self) -> typing.Tuple[Ether1616Device]:
        """:return: Get all valid and attached Ether1616 Device information. """
        rs = List[self.interface._skinning.system.Ether1616Device]()
        try:
            lst = self.interface('system.GetEther1616DeviceInfo', rs)
            return tuple(map(lambda ether: Ether1616Device(ether.IP, ether.DeviceNumber), lst))
        except ReturnCodeException as e:
            return tuple()
