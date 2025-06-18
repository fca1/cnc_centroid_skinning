import typing

# noinspection PyUnresolvedReferences
from System.Collections.Generic import List

from cncenums import Ether1616Device, UnlockVersions, MachineTypes
from exceptions.SkinningException import SkinningException
from interface.ApiInterface import ApiInterface


class Sys(ApiInterface):
    """A class for getting system-related information """

    def getSystemIdentifier(self) -> int:
        """
        :return: get the System ID of the machine to which this skinning app is connected. """
        return self._call('GetSystemIdentifier', 0)

    def exitSoftware(self):
        """Closes CNCXX software gracefully. """
        return self._call('ExitSoftware')

    # @TODO a card is needed to test this method, not yet verified
    def getEther1616DeviceInfo(self) -> typing.Tuple[Ether1616Device]:
        """:return: get all valid and attached Ether1616 Device information. """
        rs = List[Ether1616Device]()
        try:
            lst = self._call('GetEther1616DeviceInfo', rs)
            return tuple(map(lambda ether: Ether1616Device(ether.IP, ether.DeviceNumber), lst))
        except SkinningException as _e:
            return tuple()

    def getUnlockVersion(self) -> UnlockVersions:
        """:return: get the unlock version of machine connected to."""
        return self._call('GetUnlockVersion')

    def getMachineType(self) -> MachineTypes:
        """get the machine type the centroid api is connected to."""
        return self._call('GetMachineType')

    def getPLCEXP1616NumberofDevices(self) -> int:
        """gets Number of all PLCEXP1616 devices connected."""
        return self._call('GetPLCEXP1616NumberofDevices')

    def getECAT1616NumberOfDevices(self) -> int:
        """gets Number of all ECAT1616 devices connected."""
        return self._call('GetECAT1616NumberOfDevices')


    def isENCEXP12Connected(self) -> bool:
        """If ENCEXP12 connected to the AcornSix Board."""
        return self._call('IsENCEXP12Connected')

    def getSerialNumber(self) -> str:
        """get the serial number of the connected board."""
        return self._call('GetSerialNumber')


def importLicense(self, licensePath: str):
    """Import a license into cnc12."""
    return self._call('ImportLicense', licensePath)
