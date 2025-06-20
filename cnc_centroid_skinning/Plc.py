import typing

# noinspection PyUnresolvedReferences
from System import Array, String, Char, Int32, Double, Int64, UInt64, UInt32
# noinspection PyUnresolvedReferences
from System.Collections.Generic import List

from cncenums import IOMBit, BitType, ForceState, InversionState, IOState
from interface.ApiInterface import ApiInterface


class TIOMBit:
    def __init__(self, obj=None):

        self.type = None
        self.number = None
        # The state of the bit, used when returning a watch list.
        self.state = None
        self.vcpButton = None
        if obj and isinstance(obj, IOMBit):
            self.type = obj.type
            self.number = obj.number
            self.state = obj.state
            self.vcpButton = obj.vcpButton




def _fill_skinning_iombit(src:IOMBit):
    """
    :return:  TIOMBit
    """
    return TIOMBit(src)





class PLc(ApiInterface):
    """	A class with functions related to PLC programming and state information"""

    def getWatchList(self, bitList: typing.List[IOMBit]) -> [typing.List[IOMBit], None]:
        """:return:  the states of watched bits previosuly set by SetPlcWatchList """
        rs = List[IOMBit]()  # don't use the constructor with parameters
        for iombit in bitList:  # fills ref List< IOMBit > bitList
            rs.Add(_fill_skinning_iombit(iombit))
        success, lst_iombit = self._call('GetWatchList', rs, wo_rc=True)
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
        rs = List[IOMBit]()  # don't use the constructor with parameters
        for iombit in bitList:  # fills ref List< IOMBit > bitList
            insiom = IOMBit()  # CncSkinning.IOMBIT object
            rs.Add(iombit._fill_skinning_iombit(insiom))
        success, lst_iombit = self._call('SetWatchList', rs, wo_rc=True)
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
        return self._call('SetIoForceState', int(ioBit), bitType, state)

    def setSkinningDataWord(self, index: int, value: int, sendImmediately: bool = True):
        """Set a skinning data word. A skinning data word is a general purpose 32-bit integer value used to communicate
         with a PLC program. A PLC program can reference this value using the SV_SKINNING_DATA_W_1 -
         SV_SKINNING_DATA_W_12 system variables. """
        assert 1 <= index <= 12
        return self._call('SetSkinningDataWord', int(index), int(value), bool(sendImmediately))

    def getSkinningDataWord(self, index: int) -> int:
        """:return: the value of a skinning data word. """
        assert 1 <= index <= 12
        return self._call('GetSkinningDataWord', int(index), 0)

    def setSkinningDataDoubleFloatWord(self, index: int, value: float, sendImmediately: bool = True):
        """Set a skinning data float word. A skinning data float word is a general purpose 32-bit floating point value
        used to communicate with a PLC program. A PLC program can reference this value using the SV_SKINNING_DATA_FW_1
        - SV_SKINNING_DATA_FW_11 system variables. """
        return self._call('SetSkinningDataDoubleFloatWord', int(index), float(value), bool(sendImmediately))

    def getSkinningDataDoubleFloatWord(self, index: int) -> float:
        """:return: the value of a skinning float word. """
        return self._call('GetSkinningDataDoubleFloatWord', int(index))

    def setInputIversionState(self, inputBit: int, state: InversionState):
        """Set whether or not a PLC inpuit bit is inverted. """
        return self._call('SetInputInversionState', int(inputBit), state)

    def setInputForceState(self, inputBit: int, state: ForceState):
        """Set whether or not an input is forced to a given state. """
        return self._call('SetInputForceState', int(inputBit), state)

    def getInputState(self, bitNumber: int) -> bool:
        assert 1 <= bitNumber <= 1312
        """:return: the state of the PLC input """
        return self._call('GetInputState', int(bitNumber), wo_rc=True)

    def getOutputState(self, bitNumber: int) -> bool:
        """:return:  the state (On or Off) of a PLC output. """
        assert 1 <= bitNumber <= 1312
        return self._call('GetOutputState', int(bitNumber), wo_rc=True)

    def getMemoryState(self, bitNumber: int) -> bool:
        """:return:  the state of a PLC memory bit. """
        assert 1 <= bitNumber <= 1024
        return self._call('GetMemoryState', int(bitNumber), wo_rc=True)

    def getWordValue(self, index: int) -> int:
        """:return: s the value of the given PLC 32-bit integer W value. """
        assert 1 <= index <= 22
        return self._call('GetDoubleWordValue', int(index), 0)

    def getDoubleWordValue(self, index: int) -> int:
        assert 1 <= index <= 22
        return self.getWordValue(index)

    def getFloatWordValue(self, index: int) -> float:
        """:return: s the value of the given PLC 32-bit floating point FW value. """
        assert 1 <= index <= 44
        return self._call('GetDoubleFloatWordValue', int(index))

    def setSkinEventState(self, eventNumber: int, state: int):
        """Set skin event number to a given state. """
        return self._call('SetSkinEventState', int(eventNumber), int(state))

    # TODO GetPlcSystemVariableBit unknow enum  ( not declared inside the dll)
    def getPcSystemVariableBit(self, bit: int) -> IOState:
        raise RuntimeError("This method is not implemented")
        """:return:  the state of a "PC" system variable bit. A "PC" system varaible bit is, in most cases, set by the CNC
        softare running on the PC and used to communicate status to the MPU hardware, in particular the PLC system. """
        return IOState(self._call('GetPcSystemVariableBit', int(bit), 0))

    # TODO getPlcSystemVariableBit (unknow enum not declared inside the dll)
    def getPlcSystemVariableBit(self, bit: int) -> IOState:
        raise RuntimeError("This method is not implemented")
        """:return:  the state of a "PLC" system variable bit. A "PLC" system varaible bit is, in most cases, set by the PLC
         program running on the MPU hardware and used to communicate status to the CNC software. """
        return self._call('GetPlcSystemVariableBit', int(bit), 0)

    def getVcpLedStates(self) -> int:
        """:return: the state of output LEDs for the VCP all at once. """
        return self._call('GetVcpLedStates', wo_rc=True)
