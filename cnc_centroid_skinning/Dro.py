from typing import List

from cncenums import DroCoordinates
from centroidAPIInterface import CentroidAPIInterface


class Dro:
    """Class to get DRO information from CNC12. """

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    """Class to get DRO information from CNC12."""

    def getDro(self, dro_coordinates: DroCoordinates) -> List[str]:
        """:return: an array of strings containing the DRO readout from CNC12. """
        ans = self.interface('dro.GetDro', dro_coordinates, [])
        return list(map(str, ans))

    def setDroCoordinates(self, dro_coordinates: DroCoordinates):
        """Set the Dro coordinates """
        return self.interface('dro.SetDroCoordinates', dro_coordinates)
