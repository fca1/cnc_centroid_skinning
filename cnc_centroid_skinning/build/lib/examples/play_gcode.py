import sys
import locale
import ctypes
import time

from cnc_centroid_skinning.cnc_centroid_skinning.Axes import Axes
from cnc_centroid_skinning.cnc_centroid_skinning.Axis import Direction
from cnc_centroid_skinning.cnc_centroid_skinning.cncSkinning import CncSkinning
from cnc_centroid_skinning.cnc_centroid_skinning.State import UnitsOfMeasure
from cnc_centroid_skinning.cnc_centroid_skinning.exceptions.SkinningException import ReturnCodeException


def initializeApi(file_path_of_prg:str):
    sk = CncSkinning(file_path_of_prg)
    if not sk.isConstructed():
        # impossible to  communicate with CNC12 acorn
        print("the Acorn software is not launched")
        sys.exit()
    return sk


sk = initializeApi(r"C:\cnct")  # Path file of CNC12 software.

# search what is the axis with the label 'X':
x_axe = None
for axe in Axes:
    if sk.axis.getLabel(axe)=='X':
        x_axe = axe
        break
if x_axe is None:
    print("machine without X axis... no futur")
    sys.exit(0)

# units used
unit_str = ('inch', 'mm')[sk.state.getUnitsOfMeasureDefault() == UnitsOfMeasure.METRIC_UNITS]

# search the limits of x
low_limit_x     = sk.axis.getTravelLimit(x_axe,Direction.MINUS)
high_limit_x    = sk.axis.getTravelLimit(x_axe,Direction.PLUS)

#advertize inside message window of CNC12
sk.message_window.message='try to start moving'

try:
    # by this way, gcodes are immediatly taken by the CNC12
    sk.job.gcode=f'G53 G0 X{low_limit_x}',f'X{high_limit_x}'
except ReturnCodeException:
    print("this runCommand is refused (MDI,???)")
    sys.exit(0)

print(f"move X from {low_limit_x} to {high_limit_x} {unit_str}")
# Wait with the way of message_window than this RunCommand is Terminated
# it's not a good method, because an other message can be delivered after than the job is finished....
while not sk.message_window.message.startswith('306'): time.sleep(0.3) # job finished

pass

