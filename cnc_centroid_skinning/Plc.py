import typing

# noinspection PyUnresolvedReferences
from System import Array, String, Char, Int32, Double, Int64, UInt64, UInt32
# noinspection PyUnresolvedReferences
from System.Collections.Generic import List

from .cncenums import IOMBit, BitType, ForceState, InversionState, IOState
from .interface.ApiInterface import ApiInterface


class TIOMBit:
    def __init__(self, obj=None):

        self.type = None
        self.number = None
        # The state of the bit, used when returning a watch list.
        self.state = None
        self.vcpButton = None
        if obj:
            self.type = obj.type
            self.number = obj.number
            self.state = obj.state
            self.vcpButton = obj.vcpButton




class PLc(ApiInterface):
    """Class for PLC programming and state information."""

    def _to_dotnet_iombit(self, src: IOMBit):
        obj = self._interface.cls.Plc.IOMBit()
        if src.type is not None:
            obj.type = self._coerce_param(src.type)
        if src.number is not None:
            obj.number = src.number
        if src.state is not None:
            obj.state = self._coerce_param(src.state)
        if src.vcpButton is not None:
            obj.vcpButton = src.vcpButton
        return obj

    @staticmethod
    def _from_dotnet_iombit(src):
        return IOMBit(
            type=BitType(int(src.type)),
            number=src.number,
            state=IOState(int(src.state)),
            vcpButton=src.vcpButton,
        )

    def getWatchList(self, bitList: typing.List[IOMBit]) -> [typing.List[IOMBit], None]:
        """Get the states of watched bits previously set by SetWatchList."""
        rs = List[self._interface.cls.Plc.IOMBit]()  # don't use the constructor with parameters
        for iombit in bitList:  # fills ref List< IOMBit > bitList
            rs.Add(self._to_dotnet_iombit(iombit))
        success, lst_iombit = self._call('GetWatchList', rs, wo_rc=True)
        if success:
            lst_wrap = list()
            for iombit in lst_iombit:
                lst_wrap.append(self._from_dotnet_iombit(iombit))
            return lst_wrap
        else:
            return None

    def setWatchList(self, bitList: typing.List[IOMBit]) -> [typing.List[IOMBit], None]:
        """Set the PLC watch list and return the current states."""
        rs = List[self._interface.cls.Plc.IOMBit]()  # don't use the constructor with parameters
        for iombit in bitList:  # fills ref List< IOMBit > bitList
            rs.Add(self._to_dotnet_iombit(iombit))
        success, lst_iombit = self._call('SetWatchList', rs, wo_rc=True)
        if success:
            lst_wrap = list()
            for iombit in lst_iombit:
                lst_wrap.append(self._from_dotnet_iombit(iombit))
            return lst_wrap
        else:
            return None

    def setIoForceState(self, ioBit: int, bitType: BitType, state: ForceState):
        """Set the force state of an output or memory bit."""
        return self._call('SetIoForceState', int(ioBit), bitType, state)

    def setSkinningDataWord(self, index: int, value: int, sendImmediately: bool = True):
        """Set a skinning data word used to communicate with a PLC program."""
        assert 1 <= index <= 12
        return self._call('SetSkinningDataWord', int(index), int(value), bool(sendImmediately))

    def getSkinningDataWord(self, index: int) -> int:
        """Get the value of a skinning data word."""
        assert 1 <= index <= 12
        return self._call('GetSkinningDataWord', int(index))

    def setSkinningDataDoubleFloatWord(self, index: int, value: float, sendImmediately: bool = True):
        """Set a skinning floating-point data word."""
        return self._call('SetSkinningDataDoubleFloatWord', int(index), float(value), bool(sendImmediately))

    def getSkinningDataDoubleFloatWord(self, index: int) -> float:
        """Get the value of a skinning floating-point data word."""
        return self._call('GetSkinningDataDoubleFloatWord', int(index))

    def setInputInversionState(self, inputBit: int, state: InversionState):
        """Set whether a PLC input bit is inverted."""
        return self._call('SetInputInversionState', int(inputBit), state)

    def setInputIversionState(self, inputBit: int, state: InversionState):
        """Backward-compatible alias for the original misspelled method name."""
        return self.setInputInversionState(inputBit, state)

    def setInputForceState(self, inputBit: int, state: ForceState):
        """Set whether an input is forced to a given state."""
        return self._call('SetInputForceState', int(inputBit), state)

    def getInputState(self, bitNumber: int) -> bool:
        assert 1 <= bitNumber <= 1312
        """Get the state of a PLC input."""
        return self._call('GetInputState', int(bitNumber), wo_rc=True)

    def getOutputState(self, bitNumber: int) -> bool:
        """Get the state of a PLC output."""
        assert 1 <= bitNumber <= 1312
        return self._call('GetOutputState', int(bitNumber), wo_rc=True)

    def getMemoryState(self, bitNumber: int) -> bool:
        """Get the state of a PLC memory bit."""
        assert 1 <= bitNumber <= 1024
        return self._call('GetMemoryState', int(bitNumber), wo_rc=True)

    def getWordValue(self, index: int) -> int:
        """Get the given PLC 32-bit integer W value."""
        assert 1 <= index <= 22
        return self._call('GetDoubleWordValue', int(index))

    def getDoubleWordValue(self, index: int) -> int:
        assert 1 <= index <= 22
        return self.getWordValue(index)

    def getFloatWordValue(self, index: int) -> float:
        """Get the given PLC 32-bit floating point FW value."""
        assert 1 <= index <= 44
        return self._call('GetDoubleFloatWordValue', int(index))

    def setSkinEventState(self, eventNumber: int, state: int):
        """Set a skin event number to a given state."""
        return self._call('SetSkinEventState', int(eventNumber), int(state))

    # TODO Missing public enum mapping for PcToMpuSysVarBit.
    def getPcSystemVariableBit(self, bit: int) -> IOState:
        raise RuntimeError("This method is not implemented")
        """Get the state of a PC-to-MPU system variable bit."""
        return IOState(self._call('GetPcSystemVariableBit', int(bit)))

    # TODO Missing public enum mapping for MpuToPcSysVarBit.
    def getPlcSystemVariableBit(self, bit: int) -> IOState:
        raise RuntimeError("This method is not implemented")
        """Get the state of an MPU-to-PC system variable bit."""
        return self._call('GetPlcSystemVariableBit', int(bit))

    def getVcpLedStates(self) -> int:
        """Get all VCP output LED states."""
        return self._call('GetVcpLedStates', wo_rc=True)
