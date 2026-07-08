import unittest
from pathlib import Path

from cnc_centroid_skinning import PATH_CNC12


class TestEnumGenerator(unittest.TestCase):
    def test_generator_matches_checked_in_snapshot_when_dll_is_available(self):
        try:
            from tools.generate_cncenums import generate
        except Exception as exc:
            raise unittest.SkipTest(f"Enum generator is not available: {exc}") from exc

        dll_path = Path(PATH_CNC12) / "CentroidAPI.dll"
        if not dll_path.exists():
            raise unittest.SkipTest(f"CentroidAPI.dll not found at {dll_path}")

        expected = Path(__file__).resolve().parents[1] / "cnc_centroid_skinning" / "cncenums.py"
        self.assertEqual(expected.read_text(encoding="utf-8"), generate(PATH_CNC12))
