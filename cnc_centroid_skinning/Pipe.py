from interface.ApiInterface import ApiInterface


class Pipe(ApiInterface):
    """Class to get screen and viewport info """

    def isConstructed(self) -> bool:
        """:return: info from the  specified viewport """
        return self._call("IsConstructed", wo_rc=True)

    @property
    def burst_mode(self)->bool:
        return self._call("get_BurstMode", wo_rc=True)

    @burst_mode.setter
    def burst_mode(self,enable:bool):
        self._call("set_BurstMode",enable, wo_rc=True)

