


class SkinningException(Exception):
    pass


class ReturnCodeException(SkinningException):
    from cncenums import ReturnCode
    def __init__(self, message, value: ReturnCode):
        super().__init__(message)
        self.value = value
