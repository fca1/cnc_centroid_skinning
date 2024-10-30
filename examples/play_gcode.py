import sys
import time

from cnc_centroid_skinning import PATH_CNC12
from cnc_centroid_skinning.Axis import Direction
from cnc_centroid_skinning.State import UnitsOfMeasure
from cnc_centroid_skinning.centroidAPI import CentroidAPI
from cnc_centroid_skinning.enums import Axes
from cnc_centroid_skinning.exceptions.SkinningException import ReturnCodeException


def initializeApi(file_path_of_prg: str):
    sk = CentroidAPI(file_path_of_prg)
    if not sk.isConstructed():
        # impossible to  communicate with CNC12 acorn
        print("the Acorn software is not launched")
        sys.exit()
    return sk


sk = initializeApi(PATH_CNC12)  # Path file of CNC12 software.

# search what is the axis with the label 'X':
x_axe = None
for axe in Axes.values():
    if sk.axis.getLabel(axe) == 'X':
        x_axe = axe
        break
if x_axe is None:
    print("machine without X axis... no futur")
    sys.exit(0)

# units used
unit_str = ('inch', 'mm')[sk.state.getUnitsOfMeasureDefault() == UnitsOfMeasure.METRIC_UNITS]

# search the limits of x
low_limit_x = sk.axis.getTravelLimit(x_axe, Direction.MINUS)
high_limit_x = sk.axis.getTravelLimit(x_axe, Direction.PLUS)

# advertize inside message window of CNC12
sk.message_window.message = 'try to start moving'

distanceX  = (high_limit_x-low_limit_x)/10

try:
    # by this way, gcodes are immediatly taken by the CNC12
    sk.job.gcode = f'G53 G0 X{low_limit_x}', f'X{distanceX}'
except ReturnCodeException:
    print("this runCommand is refused (MDI,???)")
    sys.exit(0)

print(f"move X from {low_limit_x} to {distanceX} {unit_str}")
# Wait with the way of message_window than this RunCommand is Terminated
# it's not a good method, because an other message can be delivered after than the job is finished....
while not sk.message_window.message.startswith('306'): time.sleep(0.3)  # job finished

pass
