from interface.ApiInterface import ApiInterface


class Pipe(ApiInterface):
    """Class to get screen and viewport info """

    def isConstructed(self) -> bool:
        """:return: info from the  specified viewport """
        return self._call("IsConstructed",wo_rc=True)
