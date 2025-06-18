from typing import List

from interface.ApiInterface import ApiInterface
from cncenums import DroCoordinates


class Dro(ApiInterface):
    """Class to get DRO information from CNC12. """





    """Class to get DRO information from CNC12."""

    def getDro(self, dro_coordinates: DroCoordinates) -> List[str]:
        """:return: an array of strings containing the DRO readout from CNC12. """
        ans = self._call('dro.GetDro', dro_coordinates, [])
        return list(map(str, ans))

    def setDroCoordinates(self, dro_coordinates: DroCoordinates):
        """Set the Dro coordinates """
        return self._call('dro.SetDroCoordinates', dro_coordinates)
