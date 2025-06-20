from cnc_centroid_skinning import CNCPipe

Axes = CNCPipe.Axes
Axes.values = lambda: iter(Axes.GetValues(Axes))  # iterable

Rate = CNCPipe.Axis.Rate
WCS = CNCPipe.Wcs.WCS
Direction = CNCPipe.Axis.Direction
ReturnCode = CNCPipe.ReturnCode

CircularInterpolationDirection = CNCPipe.State.CircularInterpolationDirection
CircularInterpolationPlane = CNCPipe.State.CircularInterpolationPlane
FeedHoldState = CNCPipe.State.FeedHoldState
MdiState = CNCPipe.State.MdiState
MoveMode = CNCPipe.State.MoveMode
PositioningMode = CNCPipe.State.PositioningMode
UnitsOfMeasure = CNCPipe.State.UnitsOfMeasure
Value = CNCPipe.State.Value
HomingType = CNCPipe.State.HomingType
DroCoordinates = CNCPipe.Dro.DroCoordinates
IOMBit = CNCPipe.Plc.IOMBit

BitType = CNCPipe.Plc.BitType
ForceState = CNCPipe.Plc.ForceState
InversionState = CNCPipe.Plc.InversionState
IOState = CNCPipe.Plc.IOState
Viewport = CNCPipe.Screen.Viewport
Ether1616Device = CNCPipe.Sys.Ether1616Device
UnlockVersions = CNCPipe.Sys.UnlockVersions
MachineTypes = CNCPipe.Sys.MachineTypes



Coolant = CNCPipe.Tool.Coolant
SpindleDirection = CNCPipe.Tool.SpindleDirection
ToolWearAdjustmentType = CNCPipe.Tool.ToolWearAdjustmentType
ProbeBossOrientation = CNCPipe.Job.ProbeBossOrientation
