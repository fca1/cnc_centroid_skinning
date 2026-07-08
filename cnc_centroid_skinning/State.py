from typing import List

from .cncenums import MdiState, MoveMode, FeedHoldState, PositioningMode, UnitsOfMeasure, HomingType, Value
from .interface.ApiInterface import ApiInterface


class State(ApiInterface):
    """Holds CNC12 state info such as move mode, position mode, feedrate, and spindle speed."""

    def getScreenSize(self) -> tuple:
        """Get the CNC application screen size."""
        return self._call('GetScreenSize')

    def getMonitorSize(self) -> tuple:
        """Get the CNC application monitor size."""
        return self._call('GetMonitorSize')

    def getScreenPosition(self) -> tuple:
        """Get the CNC application screen position."""
        return self._call('GetScreenPosition')

    def getAcornBoardRevision(self) -> int:
        """Get the Acorn board revision."""
        return self._call('GetAcornBoardRevision')

    def getActiveGCodes(self) -> List[str]:
        """Get the currently active modal G- and M-codes."""
        return list(map(str, self._call('GetActiveGCodes')))

    def getFeedHoldState(self) -> FeedHoldState:
        """Get the current feed hold state."""
        return self._call('GetFeedHoldState')

    def getGCodeDisplay(self) -> List[str]:
        """Get the G-code display lines shown while a job is running."""
        return list(map(str, self._call('GetGCodeDisplay')))

    def getJobNameCurrent(self) -> str:
        """Get the name of the currently loaded job."""
        return self._call('GetJobNameCurrent')

    def getMdiState(self) -> MdiState:
        return self._call('GetMdiState')

    def getMoveMode(self) -> MoveMode:
        """Get the current move mode."""
        return self._call('GetMoveMode')

    def getPositioningMode(self) -> PositioningMode:
        """Get the current positioning mode."""
        return self._call('GetPositioningMode')

    def getUnitsOfMeasureDefault(self) -> UnitsOfMeasure:
        """Get the default units of measure from CNC12."""
        return UnitsOfMeasure(int(self._call('GetUnitsOfMeasureDefault')))

    def setImperialUnits(self):
        """Set the default unit of measure to inch."""
        return self._call('SetImperialUnits')

    def setMetricUnits(self):
        """Set the default unit of measure to metric."""
        return self._call('SetMetricUnits')

    def getUnitsOfMeasureDro(self) -> UnitsOfMeasure:
        """Get the DRO units of measure from CNC12."""
        return self._call('GetUnitsOfMeasureDro')

    def getFeedrate(self) -> float:
        """Get the measured feedrate, including feedrate override."""
        return self._call('GetFeedrate')

    def getSpindleSpeed(self) -> float:
        """Get the current spindle speed."""
        return self._call('GetSpindleSpeed')

    def getCurrentMachinePosition(self) -> [float,...]:
        """Get the current machine position."""
        machinePosition = self._call('GetCurrentMachinePosition')
        return tuple(map(float, machinePosition))

    def getFeedrateOverride(self) -> int:
        """Get the feedrate override percentage."""
        return self._call('GetFeedrateOverride')

    def getCurrentLocalPosition(self) -> [float]:
        """Get the current local WCS position."""
        return tuple(map(float, self._call('GetCurrentLocalPosition')))

    def getHighRangeSpindleSpeed(self, max_or_min: Value) -> float:
        """Get the high-range spindle speed maximum or minimum."""
        return self._call('GetHighRangeSpindleSpeed', max_or_min)

    def setHighRangeSpindleSpeed(self, max_or_min: Value, value: float):
        """Set the high-range spindle speed maximum or minimum."""
        return self._call('SetHighRangeSpindleSpeed', max_or_min, float(value))

    def getMachineHomeAtPowerUp(self) -> HomingType:
        """Get the machine homing type used at power up."""
        return self._call('GetMachineHomeAtPowerUp')

    def setMachineHomeAtPowerUp(self, homing_type: HomingType):
        """Set the machine homing type used at power up."""
        return self._call('SetMachineHomeAtPowerUp', homing_type)
