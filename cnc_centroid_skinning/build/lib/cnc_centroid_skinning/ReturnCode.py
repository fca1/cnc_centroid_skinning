from enum import IntEnum, unique


@unique
class ReturnCode(IntEnum):
    ERROR_CLIENT_LOCKED = 0
    """
    The machine is not allowed to move at this time
    """
    ERROR_INVALID_ARGUMENT = 1
    """
    The value could not be interpreted as a number by CNC12.
    """
    ERROR_INVALID_AXIS = 2
    """
    Axis was not found to be in range 1 - 8.
    """
    ERROR_INVALID_PLC_BIT_NUMBER = 3
    """
    Invalid plc bit number was selected.
    """
    ERROR_INVALID_PLC_BIT_TYPE = 4
    """
    Invalid plc bit type was selected.
    """
    ERROR_INVALID_REQUEST = 5
    """
    Request cannot be granted under current configuration.
    """
    ERROR_INVALID_SKINNING_DATA_WORD_INDEX = 6
    """
    The index was out of range.
    """
    ERROR_JOB_IN_PROGRESS = 7
    """
    A value could not be set because a job is running.
    """
    ERROR_PIPE_IS_BROKEN = 8
    """
    CNC12 closed while you were trying to use the pipe.
    """
    ERROR_PLC_SEND_SKINNING_DATA = 9
    '''
    Could not send skinning data to the plc.
    '''
    ERROR_SAVE_CONFIGURATION = 10
    """
    Could not save the configuration that was changed.
    """
    ERROR_SEND_COMMAND = 11
    """
    The command was not sent successfully to CNC12.
    """
    ERROR_SEND_PID_SETUPS = 12
    """
    CNC12 could not send PID setups to the MPU.
    """
    ERROR_SEND_SETUPS = 13
    """
    CNC12 could not send setups to the MPU.
    """
    ERROR_OUT_OF_RANGE = 14
    """
    The value is out of range for the PC.
    """
    ERROR_UNKNOWN = 15
    """
    An unknown error occurred.
    """
    ERROR_VALIDATION = 16
    """
    CNC12 could not set value because it is not valid.
    """
    STATUS_UNKNOWN = 17
    """
    Skinning API received unknown response from CNC12.
    """
    ERR_DEPRICIATED = 18
    """
    Skinning API received call to depreciated function.
    """
    SUCCESS = 19
    """
    No errors occurred.
    """
