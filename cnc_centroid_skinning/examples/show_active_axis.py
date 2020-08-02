# TODO ask why even when the reset Initiated, the return code of this command is a SUCCESS (gcode is not executed in this case)

import sys

from ..cnc_centroid_skinning import CncSkinning, UnitsOfMeasure, Axes


def initializeApi(file_path_of_prg:str):
    sk = CncSkinning(file_path_of_prg)
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
    position = sk.state.getCurrentLocalPosition()
    unit_str = ('inch', 'mm')[sk.state.getUnitsOfMeasureDefault() == UnitsOfMeasure.METRIC_UNITS]
    for axe in Axes:
        if (label := sk.axis.getLabel(axe)) == 'N':
            continue  # Axe is not declared
        sk.message_window.message = f"axe {label} position: {position[axe.value]} {unit_str}"




sk = initializeApi(r"C:\cnct")  # Path file of CNC12 software.
axis_position(sk)
