from enum import IntEnum, unique
from typing import List

from centroidAPIInterface import CentroidAPIInterface


@unique
class ProbeBossOrientation(IntEnum):
    X_PLUS = 0

    """Positive x direction."""
    Y_PLUS = 1

    """Positive y direction."""
    X_MINUS = 2

    """Negative x direction."""
    Y_MINUS = 3
    """Negative y direction."""


class Job:
    """A class for constructing and running jobs """

    def __init__(self, interface: CentroidAPIInterface):
        self.interface = interface

    def load(self, path: str):
        """Load an existing job into CNC12"""
        return self.interface('job.Load', path)

    def runCommand(self, command: str, require_cycle_start: bool = True):
        """
        Run a command now. If we require cycle start, it will post as an actual job
        .. warnings also::  If a previous runCommand is running, this call is ignored without advertizing.
        https://centroidcncforum.com/viewtopic.php?f=60&t=4607
        """
        return self.interface('job.RunCommand', command, self.interface.path_running, bool(require_cycle_start))

    @property
    def gcode(self):
        return ""

    @gcode.setter
    def gcode(self, gc: [str, List[str]]):
        """

        :param gc: str or list of str
        :return: None
        """
        if type(gc) != str:
            gc = '\n'.join(gc)
        self.runCommand(gc, require_cycle_start=False)
