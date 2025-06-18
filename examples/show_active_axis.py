# TODO ask why even when the reset Initiated, the return code of this command is a SUCCESS (gcode is not executed in this case)

import sys

from cnc_centroid_skinning import PATH_CNC12
from cnc_centroid_skinning.Axis import Axes
from centroidAPI import CentroidApi
from cnc_centroid_skinning.cncenums import UnitsOfMeasure


def initializeApi(file_path_of_prg: str):
    sk = CentroidApi(file_path_of_prg)
    if not sk.isConstructed():
        # impossible to  communicate with CNC12 acorn
        print("the Acorn software is not launched")
        sys.exit()
    return sk


def axis_position(sk):
    """
    Write inside the message window, the current position of axes
    :return:
    """
    sk.message_window.message = "*** axis position ***"
    position = sk.state.getCurrentMachinePosition()

    unit_str = ('inch', 'mm')[sk.state.getUnitsOfMeasureDefault() == UnitsOfMeasure.METRIC_UNITS]
    for axe in Axes.values():
        if (label := sk.axis.getLabel(axe)) == 'N':
            continue  # Axe is not declared
        sk.message_window.message = f"axe {label} position: {position[axe]} {unit_str}"


sk = initializeApi(PATH_CNC12)  # Path file of CNC12 software.
axis_position(sk)
