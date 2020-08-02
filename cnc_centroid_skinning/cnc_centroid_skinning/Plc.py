from dataclasses import dataclass
from enum import IntEnum, unique
import typing

from .cncSkinningInterface import CncSkinningInterface
# noinspection PyUnresolvedReferences
from System.Collections.Generic import List
# noinspection PyUnresolvedReferences
from System import Array, String, Char, Int32, Double, Int64, UInt64, UInt32


@unique
class BitType(IntEnum):
    Input = 0
    """A PLC input bit"""
    Output = 1
    """A PLC output bit"""
    Memory = 2
    """A PLC memory bit"""


@unique
class ForceState(IntEnum):
    NotForced = 0
    """The PLC bit (input/output/memory) is not forced. It is controlled by the PLC program logic."""
    ForcedOn = 1
    """The PLC bit (output/memory) is forced on/set. For input PLC bit types, this is the same as ForcedOff since inputs use the Inversion state to determine whether the input is forced on or off."""
    ForcedOff = 2
    """The PLC bit (output/memory) is forced off/reset. For input PLC bit types, this is the same as ForcedOn since inputs use the Inversion state to determine whether the input is forced on or off."""


@unique
class InversionState(IntEnum):
    NotIverted = 0
    """The    input is not inverted"""
    Inverted = 1
    """The    input is inverted"""


class IOState(IntEnum):
    IO_LOGICAL_0 = 0
    """Open or off"""
    IO_LOGICAL_1 = 1
    """Closed or on"""
    IO_INDEX_OUT_OF_RANGE = 2
    """Invalid bit index"""
    IO_STATE_UNKNOWN = 3
    """State could not be determined"""


@dataclass
class IOMBit:
    type: BitType = BitType.Input
    """A BitType enumeration """
    number: int = 0
    """Bit number. """
    state: IOState = IOState.IO_LOGICAL_0
    """The state of the bit, used when returning a watch list. """
    vcpButton: object = None
    """The VCP button object """

    def _fill_skinning_iombit(self, insiom):
        """
        :return:  CncSkinning.IOMBIT object
        """
        insiom.type = self.type  # copy all fields
        insiom.number = self.number
        insiom.state = self.state
        insiom.vcpButton = self.vcpButton
        return insiom


class PLc:
    """	A class with functions related to PLC programming and state information"""
    def __init__(self, interface: CncSkinningInterface):
        self.interface = interface

    def getWatchList(self, bitList: typing.List[IOMBit]) -> [typing.List[IOMBit], None]:
        """:return:  the states of watched bits previosuly set by SetPlcWatchList """
        rs = List[self.interface._skinning.plc.IOMBit]()  # don't use the constructor with parameters
        for iombit in bitList:  # fills ref List< IOMBit > bitList
            insiom = self.interface._skinning.plc.IOMBit()  # CncSkinning.IOMBIT object
            rs.Add(iombit._fill_skinning_iombit(insiom))
        success, lst_iombit = self.interface('plc.GetWatchList', rs, wo_rc=True)
        if success:
            lst_wrap = list()
            for iombit in lst_iombit:
                obj = IOMBit(type=iombit.type, number=iombit.number, state=iombit.state, vcpButton=iombit.vcpButton)
                lst_wrap.append(obj)
            return lst_wrap
        else:
            return None

    def setWatchList(self, bitList: typing.List[IOMBit]) -> [typing.List[IOMBit], None]:
        """Set the PLC watch list. This command also returns with the current state of the bits updated in the bitList.
        When repeated calls using the same list occur, make an initial call to SetWatchList and then retrieve the states
        using GetWatchList. """
        rs = List[self.interface._skinning.plc.IOMBit]()  # don't use the constructor with parameters
        for iombit in bitList:  # fills ref List< IOMBit > bitList
            insiom = self.interface._skinning.plc.IOMBit()  # CncSkinning.IOMBIT object
            rs.Add(iombit._fill_skinning_iombit(insiom))
        success, lst_iombit = self.interface('plc.SetWatchList', rs, wo_rc=True)
        if success:
            lst_wrap = list()
            for iombit in lst_iombit:
                obj = IOMBit(type=iombit.type, number=iombit.number, state=iombit.state, vcpButton=iombit.vcpButton)
                lst_wrap.append(obj)
            return lst_wrap
        else:
            return None

    def setIoForceState(self, ioBit: int, bitType: BitType, state: ForceState):
        """Set the state of output or memory bit forcing. Note that for memory bit types, the forcing occurs at the
        beginning of a PLC program IOMpass only, i.e., PLC code can still change the state of the memory bit if desired. """
        return self.interface('plc.SetIoForceState', int(ioBit), bitType.value, state.value)

    def setSkinningDataWord(self, index: int, value: int, sendImmediately: bool = True):
        """Set a skinning data word. A skinning data word is a general purpose 32-bit integer value used to communicate
         with a PLC program. A PLC program can reference this value using the SV_SKINNING_DATA_W_1 -
         SV_SKINNING_DATA_W_12 system variables. """
        assert 1 <= index <= 12
        return self.interface('plc.SetSkinningDataWord', int(index), int(value), bool(sendImmediately))

    def getSkinningDataWord(self, index: int) -> int:
        """:return: the value of a skinning data word. """
        assert 1 <= index <= 12
        return self.interface('plc.GetSkinningDataWord', int(index), 0)

    def setSkinningDataDoubleFloatWord(self, index: int, value: float, sendImmediately: bool = True):
        """Set a skinning data float word. A skinning data float word is a general purpose 32-bit floating point value
        used to communicate with a PLC program. A PLC program can reference this value using the SV_SKINNING_DATA_FW_1
        - SV_SKINNING_DATA_FW_11 system variables. """
        return self.interface('plc.SetSkinningDataDoubleFloatWord', int(index), float(value), bool(sendImmediately))

    def getSkinningDataDoubleFloatWord(self, index: int) -> float:
        """:return: the value of a skinning float word. """
        return self.interface('plc.GetSkinningDataDoubleFloatWord', int(index), 0.0)

    def setInputIversionState(self, inputBit: int, state: InversionState):
        """Set whether or not a PLC inpuit bit is inverted. """
        return self.interface('plc.SetInputIversionState', int(inputBit), state.value)

    def setInputForceState(self, inputBit: int, state: ForceState):
        """Set whether or not an input is forced to a given state. """
        return self.interface('plc.SetInputForceState', int(inputBit), state.value)

    def getInputState(self, bitNumber: int) -> bool:
        assert 1 <= bitNumber <= 1312
        """:return: the state of the PLC input """
        return self.interface('plc.GetInputState', int(bitNumber), wo_rc=True)

    def getOutputState(self, bitNumber: int) -> bool:
        """:return:  the state (On or Off) of a PLC output. """
        assert 1 <= bitNumber <= 1312
        return self.interface('plc.GetOutputState', int(bitNumber), wo_rc=True)

    def getMemoryState(self, bitNumber: int) -> bool:
        """:return:  the state of a PLC memory bit. """
        assert 1 <= bitNumber <= 1024
        return self.interface('plc.GetMemoryState', int(bitNumber), wo_rc=True)

    def getWordValue(self, index: int) -> int:
        """:return: s the value of the given PLC 32-bit integer W value. """
        assert 1 <= index <= 22
        return self.interface('plc.GetDoubleWordValue', int(index), 0)

    def getDoubleWordValue(self, index: int) -> int:
        assert 1 <= index <= 22
        return self.getWordValue(index)

    def getFloatWordValue(self, index: int) -> float:
        """:return: s the value of the given PLC 32-bit floating point FW value. """
        assert 1 <= index <= 44
        return self.interface('plc.GetDoubleFloatWordValue', int(index), 0.0)

    def setSkinEventState(self, eventNumber: int, state: int):
        """Set skin event number to a given state. """
        return self.interface('plc.SetSkinEventState', int(eventNumber), int(state))

    def getPcSystemVariableBit(self, bit: int) -> IOState:
        """:return:  the state of a "PC" system variable bit. A "PC" system varaible bit is, in most cases, set by the CNC
        softare running on the PC and used to communicate status to the MPU hardware, in particular the PLC system. """
        return IOState(self.interface('plc.GetPcSystemVariableBit', int(bit), 0))

    def getPlcSystemVariableBit(self, bit: int) -> IOState:
        """:return:  the state of a "PLC" system variable bit. A "PLC" system varaible bit is, in most cases, set by the PLC
         program running on the MPU hardware and used to communicate status to the CNC software. """
        return self.interface('plc.GetPlcSystemVariableBit', int(bit), 0)

    def getVcpLedStates(self) -> int:
        """:return: the state of output LEDs for the VCP all at once. """
        return self.interface('plc.GetVcpLedStates', wo_rc=True)
