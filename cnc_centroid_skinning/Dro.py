from typing import List

from CncPipe import CncPipe
from centroidAPIInterface import CentroidAPIInterface
from enums import DroCoordinates


class Dro(CncPipe):
    """Class to get DRO information from CNC12. """

    def __init__(self, interface: CentroidAPIInterface):
        super().__init__("dro", interface)

    """Class to get DRO information from CNC12."""

    def getDro(self, dro_coordinates: DroCoordinates) -> List[str]:
        """:return: an array of strings containing the DRO readout from CNC12. """
        ans = self._call_interface('GetDro', dro_coordinates, [])
        return list(map(str, ans))

    def setDroCoordinates(self, dro_coordinates: DroCoordinates):
        """Set the Dro coordinates """
        return self._call_interface('SetDroCoordinates', dro_coordinates)
