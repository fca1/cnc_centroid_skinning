import ctypes
import locale
import sys

from cnc_centroid_skinning import PATH_CNC12

from centroidAPI import CentroidApi

"""
Ask to windows os, the locale language, and if referenced, set the language of CNC12 in accordance
"""


def initializeApi(file_path_of_prg: str):
    """

    :param file_path_of_prg:  (path where cncskinning.dll
    :return:
    """
    sk = CentroidApi(file_path_of_prg)
    if not sk.isConstructed():
        # impossible to  communicate with CNC12 acorn
        print("the Acorn software is not launched")
        sys.exit()
    return sk


def change_language(sk, lang):
    """

    :param sk:
    :param lang: string litteral of language for the CNC interface (need a restart of CNC12 software)
    :return:
    """
    tbl_language = (
        'en_',
        'es_',
        'fr_',
        'zh_CHT',
        'zh_CHS',
        "de_",
        'sv_',
        'fi_',
        'pt_',
        'el_')
    for index, str_lang in enumerate(tbl_language):
        if lang.startswith(str_lang):
            if sk.parameter[9] == index:
                print("Your locale is already configurated")
                return False
            sk.parameter[9] = index  # see 12.3.11 Parameter 9 – Display Language
            return True
    print(f"this locale is not (yet) supported")
    return False


sk = initializeApi(PATH_CNC12)  # Path file of CNC12 software.

# search the local language of os
windll = ctypes.windll.kernel32
lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]
# change the parameter and change (if possible) the language
if change_language(sk, lang):
    # Exit from  CNC12 software (restart is needed)
    sk.sys.exitSoftware(sk)
