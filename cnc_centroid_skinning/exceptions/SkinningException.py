from cncenums import ReturnCode


class SkinningException(Exception):
    pass


class ReturnCodeException(SkinningException):
    def __init__(self, message, value: ReturnCode):
        super().__init__(message)
        self.value = value
