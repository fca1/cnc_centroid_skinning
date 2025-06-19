import sys
import time

from cnc_centroid_skinning.Plc import BitType, ForceState
from cnc_centroid_skinning.exceptions.SkinningException import ReturnCodeException
from cnc_centroid_skinning import PATH_CNC12
from centroidAPI import CentroidApi

def initializeApi(file_path_of_prg: str):
    _sk = CentroidApi(file_path_of_prg)
    if not _sk.isConstructed():
        # impossible to  communicate with CNC12 acorn
        print("the Acorn software is not launched")
        sys.exit()
    return _sk


sk = initializeApi(PATH_CNC12)  # Path file of CNC12 software.

# Output 6 is forced to produce a pulse of 5 sec.
try:
    sk.plc.setIoForceState(6, BitType.Output, ForceState.NotForced)
except ReturnCodeException as e:
    print(f'this output seems cannot be forced : {e}')
    sys.exit(1)
sk.plc.setIoForceState(6, BitType.Output, ForceState.ForcedOff)
time.sleep(5)
sk.plc.setIoForceState(6, BitType.Output, ForceState.NotForced)
sk.plc.setIoForceState(6, BitType.Output, ForceState.ForcedOn)
