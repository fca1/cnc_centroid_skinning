from .interface.ApiInterface import ApiInterface


class CncPipe:
    # Tracks wrapper classes referenced from CNCPipe.
    _list_cncPipe = set()

    def __init__(self, name_class: str, interface: ApiInterface):
        self.name_class = name_class
        self.interface = interface
        self._list_cncPipe.add(self)

        pass

    def _debug_find_new_methods(self):
        """
        Return API methods exposed by CentroidAPI but not wrapped here.
        """
        thelistCentroid = self.interface._getListFcntApi(self.name_class)
        methods = set(m for m in dir(self) if callable(getattr(self, m)) and not m.startswith("_"))
        # Compare method names case-insensitively.
        setCentroidminus = set(m.lower() for m in thelistCentroid)
        setMethodsminus = set(m.lower() for m in methods)
        return setCentroidminus - setMethodsminus

    @staticmethod
    def childs() -> set:
        return CncPipe._list_cncPipe

    def _call_interface(self, nameMethod: str, *params,**kwargs) -> [tuple,float,int]:
        """Forward a method call to the wrapped interface."""
        rest_lst = self.interface(f'{self.name_class}.{nameMethod}',*params,**kwargs)
        return rest_lst
