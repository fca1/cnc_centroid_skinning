import typing

# noinspection PyUnresolvedReferences
from System.Collections.Generic import List

from interface.ApiInterface import ApiInterface
from cncenums import Ether1616Device
from exceptions.SkinningException import SkinningException


class Sys(ApiInterface):
    """A class for getting system-related information """


    def getSystemIdentifier(self) -> int:

        """
        :return: Get the System ID of the machine to which this skinning app is connected. """
        return self._call('system.GetSystemIdentifier', 0)

    def exitSoftware(self):
        """Closes CNCXX software gracefully. """
        return self._call('system.ExitSoftware')

    # @TODO a card is needed to test this method, not yet verified
    def getEther1616DeviceInfo(self) -> typing.Tuple[Ether1616Device]:
        """:return: Get all valid and attached Ether1616 Device information. """
        rs = List[self._call._skinning.system.Ether1616Device]()
        try:
            lst = self._call('system.GetEther1616DeviceInfo', rs)
            return tuple(map(lambda ether: Ether1616Device(ether.IP, ether.DeviceNumber), lst))
        except SkinningException as _e:
            return tuple()
