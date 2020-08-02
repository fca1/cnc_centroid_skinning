import sys
import locale
import ctypes

from ..cncSkinning import CncSkinning



def initializeApi(file_path_of_prg:str):
    sk = CncSkinning(file_path_of_prg)
    if not sk.isConstructed():
        # impossible to  communicate with CNC12 acorn
        print("the Acorn software is not launched")
        sys.exit()
    return sk

def hardware(sk):
    """
    Write inside the message window of CNC12, identification and misc.
    :return:
    """
    sk.message_window.message = "*** hardware ***"
    sk.message_window.addMessage(f"System identifier :\t{sk.system.getSystemIdentifier()}",
                                 backgroundColor=0x000040)  # TODO understand why colors don't change
    sk.message_window.message = f"Board revision    :\t{sk.state.getAcornBoardRevision()}"
    sk.message_window.message = f"Nber of Ether1616 :\t{len(sk.system.getEther1616DeviceInfo())}"



sk = initializeApi(r"C:\cnct")  # Path file of CNC12 software.
hardware(sk)