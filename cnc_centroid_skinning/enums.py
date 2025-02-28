from cnc_centroid_skinning import CNCPipe

Axes = CNCPipe.Axes
Axes.values = lambda: iter(Axes.GetValues(Axes))

Rate = CNCPipe.Axis.Rate
WCS = CNCPipe.Wcs.WCS
Direction = CNCPipe.Axis.Direction
ReturnCode = CNCPipe.ReturnCode
CircularInterpolationPlane = CNCPipe.State.CircularInterpolationPlane
CircularInterpolationDirection = CNCPipe.State.CircularInterpolationDirection
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

Coolant = CNCPipe.Tool.Coolant
SpindleDirection = CNCPipe.Tool.SpindleDirection
ToolWearAdjustmentType = CNCPipe.Tool.ToolWearAdjustmentType

MachineTypes = CNCPipe.Sys.MachineTypes
UnlockVersions = CNCPipe.Sys.UnlockVersions

MotorPower = CNCPipe.Axis.MotorPower

ConsoleTypes = CNCPipe.Axis.State.ConsoleTypes