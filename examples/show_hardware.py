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


def hardware(sk):
    """
    Write inside the message window of CNC12, identification and misc.
    :return:
    """
    sk.message_window.message = "*** hardware ***"
    sk.message_window.addMessage(f"System identifier :\t{sk.sys.getSystemIdentifier()}",
                                 backgroundColor=0xFFFFFF)
    sk.message_window.addMessage(f"unlockVersion :\t{sk.sys.getUnlockVersion()}")
    sk.message_window.message = f"Machine type      :\t{sk.sys.getMachineType()}"
    sk.message_window.message = f"Serial nber       :\t{sk.sys.getSerialNumber()}"
    sk.message_window.message = f"Board revision    :\t{sk.state.getAcornBoardRevision()}"
    sk.message_window.message = f"Nber of Ether1616 :\t{len(sk.sys.getEther1616DeviceInfo())}"


sk = initializeApi(PATH_CNC12)  # Path file of CNC12 software.
hardware(sk)
