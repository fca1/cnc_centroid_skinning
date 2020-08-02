import sys
import locale
import ctypes

from cnc_centroid_skinning.cnc_centroid_skinning.cncSkinning import CncSkinning


def initializeApi(file_path_of_prg:str):
    sk = CncSkinning(file_path_of_prg)
    if not sk.isConstructed():
        # impossible to  communicate with CNC12 acorn
        print("the Acorn software is not launched")
        sys.exit()
    return sk

def send_active_code(sk):
    # play gcode immediatly (if single block is not set)
    sk.job.runCommand("G4 P5.0", require_cycle_start=False)  # Wait until 5 sec.
    pass


sk = initializeApi(r"C:\cnct")  # Path file of CNC12 software.
send_active_code(sk)
