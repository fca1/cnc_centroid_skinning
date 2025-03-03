import typing

# noinspection PyUnresolvedReferences
from System.Collections.Generic import List

from CncPipe import CncPipe
from centroidAPIInterface import CentroidAPIInterface
from enums import Ether1616Device, MachineTypes, UnlockVersions
from exceptions.SkinningException import SkinningException


class Sys(CncPipe):
    """A class for getting system-related information """

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("system", interface)

    def getSystemIdentifier(self) -> int:

        """
        :return: Get the System ID of the machine to which this skinning app is connected. """
        return self._call_interface('GetSystemIdentifier', 0)

    def exitSoftware(self):
        """Closes CNCXX software gracefully. """
        return self._call_interface('ExitSoftware')

    # @TODO a card is needed to test this method, not yet verified
    def getEther1616DeviceInfo(self) -> typing.Tuple[Ether1616Device]:
        """:return: Get all valid and attached Ether1616 Device information. """
        rs = List[self.interface.skinning.system.Ether1616Device]()
        try:
            lst = self._call_interface('GetEther1616DeviceInfo', rs)
            return tuple(map(lambda ether: Ether1616Device(ether.IP, ether.DeviceNumber), lst))
        except SkinningException as _e:
            return tuple()

    def getECAT1616NumberOfDevices(self) -> int:
        """Gets Number of all ECAT1616 devices connected. """
        return self._call_interface('GetECAT1616NumberOfDevices')

    def getMachineType(self) -> MachineTypes:
        """ Get the machine type the centroid api is connected to. """
        return self._call_interface('GetMachineType')

    def getSerialNumber(self) -> str:
        """ Get the serial number of the connected board. """
        return self._call_interface('GetSerialNumber')

    def getUnlockVersion(self) -> UnlockVersions:
        return self._call_interface('GetUnlockVersion')

    def importLicense(self, licensePath: str):
        return self._call_interface('ImportLicense', licensePath)

    def isENCEXP12Connected(self) -> bool:
        return self._call_interface('IsENCEXP12Connected')

    def getPLCEXP1616NumberofDevices(self) -> int:
        """Gets Number of all PLCEXP1616 devices connected."""
        return self._call_interface('GetPLCEXP1616NumberofDevices')
