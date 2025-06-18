from typing import List

from cncenums import DroCoordinates
from interface.ApiInterface import ApiInterface


class Dro(ApiInterface):
    """Class to get DRO information from CNC12. """

    """Class to get DRO information from CNC12."""

    def getDro(self, dro_coordinates: DroCoordinates) -> List[str]:
        """:return: an array of strings containing the DRO readout from CNC12. """
        ans = self._call('GetDro', dro_coordinates, [])
        return list(map(str, ans))

    def setDroCoordinates(self, dro_coordinates: DroCoordinates):
        """Set the Dro coordinates """
        return self._call('SetDroCoordinates', dro_coordinates)
