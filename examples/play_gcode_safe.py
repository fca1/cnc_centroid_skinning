import sys

from cnc_centroid_skinning import PATH_CNC12
from centroidAPI import CentroidApi


def initializeApi(file_path_of_prg: str):
    _sk = CentroidApi(file_path_of_prg)
    if not _sk.isConstructed():
        # impossible to  communicate with CNC12 acorn
        print("the Acorn software is not launched")
        sys.exit()
    return _sk


def send_active_code(sk):
    # play gcode immediatly (if single block is not set)
    result = sk.state.getMdiState()
    sk.job.runCommand("G4 P5.0", require_cycle_start=False)  # Wait until 5 sec.
    result = sk.state.getMdiState()
    pass


sk = initializeApi(PATH_CNC12)  # Path file of CNC12 software.
send_active_code(sk)
