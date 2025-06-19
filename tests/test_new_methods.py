import unittest

from cnc_centroid_skinning import PATH_CNC12, CentroidApi


class MyTestCase(unittest.TestCase):
    def test_methods(self):
        sk = CentroidApi(PATH_CNC12)
        from CncPipe import CncPipe
        for cncp in CncPipe.childs():
            print(f"class {cncp.name_class}")
            lst_new_methods = cncp._debug_find_new_methods()
            print(lst_new_methods)
            pass
        pass
