from .interface.ApiInterface import ApiInterface


class Pipe(ApiInterface):
    """Root CNCPipe helpers."""

    def isConstructed(self) -> bool:
        """Return whether the CNCPipe instance was constructed successfully."""
        return self._call("IsConstructed", wo_rc=True)

    @property
    def burst_mode(self)->bool:
        return self._skinning.BurstMode

    @burst_mode.setter
    def burst_mode(self,enable:bool):
        self._skinning.BurstMode = bool(enable)

    def startListening(self):
        """Start listening for inbound CNC12 messages."""
        return self._call("StartListening", wo_rc=True)

    def stopListening(self):
        """Stop listening for inbound CNC12 messages."""
        return self._call("StopListening", wo_rc=True)

    def clearUnhandledMessages(self):
        """Clear queued inbound CNC12 messages that have not been handled."""
        return self._call("ClearUnhandledMessages", wo_rc=True)

    def tryPopUnhandledMessage(self):
        """Return (has_message, packet) when an inbound message is available."""
        return self._call("TryPopUnhandledMessage", wo_rc=True)

