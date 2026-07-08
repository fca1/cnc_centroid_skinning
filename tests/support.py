import unittest

from cnc_centroid_skinning import PATH_CNC12, CentroidApi


def make_api_or_skip():
    api = CentroidApi(PATH_CNC12)
    if not api.isConstructed():
        raise unittest.SkipTest("CNC12 is not running or the CNCPipe is not constructed.")
    return api
