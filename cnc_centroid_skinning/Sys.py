
# noinspection PyUnresolvedReferences
from .cncenums import Ether1616Device, UnlockVersions, MachineTypes
from .exceptions.SkinningException import SkinningException
from .interface.ApiInterface import ApiInterface


class Sys(ApiInterface):
    """Class for system-related information."""

    def getSystemIdentifier(self) -> int:
        """Get the system ID of the connected machine."""
        return self._call('GetSystemIdentifier')

    def exitSoftware(self):
        """Close CNC12 software gracefully."""
        return self._call('ExitSoftware')

    # TODO Needs hardware to verify.
    def getEther1616DeviceInfo(self) -> [Ether1616Device]:
        """Get attached Ether1616 device information."""
        try:
            lst = self._call('GetEther1616DeviceInfo')
            return tuple(map(lambda ether: Ether1616Device(ether.IP, ether.DeviceNumber), lst))
        except SkinningException as _e:
            return tuple()

    def getUnlockVersion(self) -> UnlockVersions:
        """Get the unlock version of the connected machine."""
        return self._call('GetUnlockVersion')

    def getMachineType(self) -> MachineTypes:
        """Get the machine type connected to the CentroidAPI."""
        return self._call('GetMachineType')

    def getPLCEXP1616NumberofDevices(self) -> int:
        """Get the number of connected PLCEXP1616 devices."""
        return self._call('GetPLCEXP1616NumberofDevices')

    def getECAT1616NumberOfDevices(self) -> int:
        """Get the number of connected ECAT1616 devices."""
        return self._call('GetECAT1616NumberOfDevices')


    def isENCEXP12Connected(self) -> bool:
        """Return whether ENCEXP12 is connected to the AcornSix board."""
        return self._call('IsENCEXP12Connected')

    def getSerialNumber(self) -> str:
        """Get the serial number of the connected board."""
        return self._call('GetSerialNumber')


    def importLicense(self, licensePath: str):
        """Import a license into CNC12."""
        return self._call('ImportLicense', licensePath)
