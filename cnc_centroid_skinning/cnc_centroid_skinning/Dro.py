from enum import IntEnum, unique
from typing import List

from .cncSkinningInterface import CncSkinningInterface


@unique
class DroCoordinates(IntEnum):
    """The different types of information the DRO can provide. """
    DRO_LOCAL = 0
    """Coordinates from selected wcs"""
    DRO_MACHINE = 1
    """Machine coordinates"""
    DRO_DISTANCE_TO_GO = 2
    """Values from the Distance-to-Go Dro."""


class Dro:
    """Class to get DRO information from CNC12. """
    def __init__(self, interface: CncSkinningInterface):
        self.interface = interface

    """Class to get DRO information from CNC12."""

    def getDro(self, dro_coordinates: DroCoordinates) -> List[str]:
        """:return: an array of strings containing the DRO readout from CNC12. """
        ans = self.interface('dro.GetDro', dro_coordinates.value, [])
        return list(map(str, ans))

    def setDroCoordinates(self, dro_coordinates: DroCoordinates):
        """Set the Dro coordinates """
        return self.interface('dro.SetDroCoordinates', dro_coordinates.value)
