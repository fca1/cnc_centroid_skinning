from .cncenums import DroCoordinates, JobInfoType
from .interface.ApiInterface import ApiInterface


class InboundComm(ApiInterface):
    """Handles inbound communications from CNC12."""

    def changeDroType(self, coords: DroCoordinates):
        """Set the DRO coordinates reported by CNC12 inbound communication."""
        return self._call("ChangeDroType", coords)

    def changeJobInfoType(self, info_type: JobInfoType):
        """Set the job info level reported by CNC12 inbound communication."""
        return self._call("ChangeJobInfoType", info_type)

    def ticksToDateTime(self, ticks: int):
        """Convert packet ticks to a .NET DateTime."""
        return self._call("TicksToDateTime", int(ticks), wo_rc=True)
