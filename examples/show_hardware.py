import sys
from pathlib import Path

from cnc_centroid_skinning import PATH_CNC12
from cnc_centroid_skinning.centroidAPI import CentroidAPI


def initializeApi(file_path_of_prg: str):
    _cnc_folder_path = Path(file_path_of_prg)
    if not _cnc_folder_path.exists() or not _cnc_folder_path.is_dir():
        sys.stderr.write(f"acorn {file_path_of_prg} folder is not detected ")
        sys.exit(1)

    _sk = CentroidAPI(file_path_of_prg)
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
    sk.message_window.addMessage(f"System identifier :\t{sk.system.getSystemIdentifier()}",
                                 textColor=0x00FF00)  # color is used only for the last line showed
    sk.message_window.message = f"Board revision    :\t{sk.state.getAcornBoardRevision()}"
    sk.message_window.message = f"Nber of Ether1616 :\t{len(sk.system.getEther1616DeviceInfo())}"
    pass

# Check if PATH_CNC12 is correct or change with a new path folder ( r"c:\cncm" or r"c:\cnct")
sk = initializeApi(PATH_CNC12)  # Path file of CNC12 software.
hardware(sk)
