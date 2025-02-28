
from centroidAPIInterface import CentroidAPIInterface


class CncPipe:
    # knows all referenced classes from CNCPipe
    _list_cncPipe = set()

    def __init__(self,name_class:str, interface: CentroidAPIInterface):
        self.name_class = name_class
        self.interface = interface
        self._list_cncPipe.add(self)

        pass

    def _debug_find_new_methods(self):
        """
        Used for retrieve the new instanciate methods of CNC centroid's API.
        :return:
        """
        thelistCentroid = self.interface._getListFcntApi(self.name_class)
        methods = set(m for m in dir(self) if callable(getattr(self, m)) and not m.startswith("_"))
        # The name of methods are the same except lower or upper chars
        setCentroidminus = set(m.lower() for m in thelistCentroid)
        setMethodsminus = set(m.lower() for m in methods)
        return setCentroidminus-setMethodsminus

    @staticmethod
    def childs() -> set:
        return CncPipe._list_cncPipe


    def _call_interface(self,nameMethod:str,*params) -> tuple:
        """:return: the screen size of the CNC application. """
        return self.interface(f'{self.name_class}.{nameMethod}', *params)

