from .cncenums import DroCoordinates, JobInfoType
from .interface.ApiInterface import ApiInterface


class InboundComm(ApiInterface):
    """Handles inbound communications from CNC12.

    Requires CNC12 v5.40 or later.
    """

    def changeDroType(self, coords: DroCoordinates):
        """Set the DRO coordinates reported by inbound communication. Requires CNC12 v5.40+."""
        return self._call("ChangeDroType", coords)

    def changeJobInfoType(self, info_type: JobInfoType):
        """Set the job info level reported by inbound communication. Requires CNC12 v5.40+."""
        return self._call("ChangeJobInfoType", info_type)

    def ticksToDateTime(self, ticks: int):
        """Convert packet ticks to a .NET DateTime. Requires CNC12 v5.40.03+."""
        return self._call("TicksToDateTime", int(ticks), wo_rc=True)
