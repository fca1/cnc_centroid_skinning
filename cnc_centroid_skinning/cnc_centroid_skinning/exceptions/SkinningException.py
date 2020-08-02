from .. import ReturnCode


class SkinningException(Exception):
    """ Common base class for all return code exceptions."""
    pass


class ReturnCodeException(SkinningException):
    def __init__(self, message, value: ReturnCode):
        '''
        """
        :param message: litteral message.
        :param value: The value of return code else than SUCCESS
        '''
        super().__init__(message)
        self.value = value
