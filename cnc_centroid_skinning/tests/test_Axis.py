from unittest import TestCase

from PyCncSkinning.PyCncSkinning.Axes import Axes
from PyCncSkinning.PyCncSkinning.Axis import Rate, Direction
from PyCncSkinning.PyCncSkinning.Skinning import Skinning


class TestAxis(TestCase):
    assembly_path = r"C:\cnct"
    axis = Skinning(assembly_path).axis

    def test_get_accel_time(self):
        self.axis.setAccelTime(Axes.AXIS_1, 0.43)
        self.axis.setAccelTime(Axes.AXIS_2, 0.34)
        self.assertEqual(self.axis.getAccelTime(Axes.AXIS_1), 0.43, "Accel time not set correctly")
        self.assertEqual(self.axis.getAccelTime(Axes.AXIS_2), 0.34, "Accel time not set correctly")

    def test_get_deadstart_velocity(self):
        self.axis.setDeadstartVelocity(Axes.AXIS_1, 131)
        self.axis.setDeadstartVelocity(Axes.AXIS_2, 135)
        self.assertEqual(self.axis.getDeadstartVelocity(Axes.AXIS_1), 131)
        self.assertEqual(self.axis.getDeadstartVelocity(Axes.AXIS_2), 135)

    def test_get_delta_vmax(self):
        self.axis.setDeltaVMax(Axes.AXIS_1, 131)
        self.axis.setDeltaVMax(Axes.AXIS_2, 135)
        self.assertEqual(self.axis.getDeltaVMax(Axes.AXIS_1), 131)
        self.assertEqual(self.axis.getDeltaVMax(Axes.AXIS_2), 135)

    def test_get_rate(self):
        self.axis.setRate(Axes.AXIS_2, Rate.SLOW_JOG, 120)
        self.assertEqual(self.axis.getRate(Axes.AXIS_2, Rate.SLOW_JOG), 120)
        self.axis.setRate(Axes.AXIS_2, Rate.SLOW_JOG, 240)
        self.assertEqual(self.axis.getRate(Axes.AXIS_2, Rate.SLOW_JOG), 240)

    def test_get_label(self):
        self.axis.setLabel(Axes.AXIS_2, "Y")
        self.assertEqual(self.axis.getLabel(Axes.AXIS_2), 'Y')
        self.axis.setLabel(Axes.AXIS_2, "X")
        self.assertEqual(self.axis.getLabel(Axes.AXIS_2), 'X')

    def test_get_lash_comp(self):
        self.axis.setLashComp(Axes.AXIS_2, 1)
        self.assertEqual(self.axis.getLashComp(Axes.AXIS_2), 1)
        self.axis.setLashComp(Axes.AXIS_2, 0)
        self.assertEqual(self.axis.getLashComp(Axes.AXIS_2), 0)

    def test_get_screw_pitch(self):
        self.axis.SetScrewPitch(Axes.AXIS_2, 2.22)
        self.assertEqual(self.axis.getScrewPitch(Axes.AXIS_2), 2.22)
        self.axis.SetScrewPitch(Axes.AXIS_2, 3.22)
        self.assertEqual(self.axis.getScrewPitch(Axes.AXIS_2), 3.22)

    def test_get_limit(self):
        self.axis.setLimit(Axes.AXIS_2, Direction.MINUS, 12)
        self.axis.setLimit(Axes.AXIS_2, Direction.PLUS, 23)
        self.assertEqual(self.axis.getLimit(Axes.AXIS_2, Direction.PLUS), 23)
        self.assertEqual(self.axis.getLimit(Axes.AXIS_2, Direction.MINUS), 12)

    def test_get_home_limit(self):
        self.axis.setHomeLimit(Axes.AXIS_2, Direction.PLUS, 21)
        self.axis.setHomeLimit(Axes.AXIS_2, Direction.MINUS, 42)
        self.assertEqual(self.axis.getHomeLimit(Axes.AXIS_2, Direction.PLUS), 21)
        self.assertEqual(self.axis.getHomeLimit(Axes.AXIS_2, Direction.MINUS), 42)

    def test_get_axis_reversal(self):
        r = self.axis.getAxisReversal(Axes.AXIS_2)
        self.axis.setAxisReversal(Axes.AXIS_2, not r)
        self.assertNotEqual(r, self.axis.getAxisReversal(Axes.AXIS_2))
        self.axis.setAxisReversal(Axes.AXIS_2, r)
        self.assertEqual(r, self.axis.getAxisReversal(Axes.AXIS_2))

    def test_get_counts_per_turn(self):
        cnt = self.axis.getCountsPerTurn(Axes.AXIS_2)
        self.axis.setCountsPerTurn(Axes.AXIS_2, 2 * cnt)
        self.assertEqual(2 * cnt, self.axis.getCountsPerTurn(Axes.AXIS_2))
        self.axis.setCountsPerTurn(Axes.AXIS_2, cnt)
        self.assertEqual(cnt, self.axis.getCountsPerTurn(Axes.AXIS_2))

    def test_get_travel_limit(self):
        tl = self.axis.getTravelLimit(Axes.AXIS_2, Direction.PLUS)
        self.axis.setTravelLimit(Axes.AXIS_2, Direction.PLUS, 2 * tl)
        self.assertEqual(2 * tl, self.axis.getTravelLimit(Axes.AXIS_2, Direction.PLUS))
        self.axis.setTravelLimit(Axes.AXIS_2, Direction.PLUS, tl)
        self.assertEqual(tl, self.axis.getTravelLimit(Axes.AXIS_2, Direction.PLUS))
