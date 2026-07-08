import unittest
import subprocess
import sys

import cnc_centroid_skinning as cnc
from cnc_centroid_skinning import Axes, BitType, IOMBit, JobInfoType, ReturnCode


class TestStaticPackage(unittest.TestCase):
    def test_importing_static_enums_does_not_load_centroidapi(self):
        code = (
            "from cnc_centroid_skinning import Axes; "
            "from cnc_centroid_skinning.runtime import get_loaded_centroid_api_path; "
            "print(Axes.AXIS_1); "
            "print(get_loaded_centroid_api_path())"
        )
        result = subprocess.run(
            [sys.executable, "-c", code],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(["0", "None"], result.stdout.strip().splitlines())
        self.assertEqual("0.5.42", cnc.__version__)

    def test_generated_enums_expose_expected_values(self):
        self.assertEqual(0, int(Axes.AXIS_1))
        self.assertEqual(30, int(ReturnCode.SUCCESS))
        self.assertEqual(1, int(BitType.Output))
        self.assertEqual(1, int(JobInfoType.TOP_LEVEL))
        self.assertEqual(list(Axes), list(Axes.values()))

    def test_iombit_is_importable_without_centroidapi(self):
        bit = IOMBit(type=BitType.Output, number=7)
        self.assertEqual(BitType.Output, bit.type)
        self.assertEqual(7, bit.number)
