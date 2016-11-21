"""
spinners.py module for prog_rock
"""

# Standard library imports
from __future__ import (
    absolute_import, division, print_function, unicode_literals
)
from functools import partial
import collections
import contextlib
import logging

# Third party imports

# Local imports
from . import base, printers, sequences


log = logging.getLogger(__name__)


class Spinner:
    """A generic spinner class"""

    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def tick(self):
        """Tick"""
        if self._index == len(self._sequence):
            self._index = 0
        printers.printf(self._sequence[self._index][0])
        self._sequence[self._index][1]()
        self._index += 1

    def run_until_signaled(self, event=None):
        """

        :return:
        """
        if self.event is None:
            raise RuntimeError
        while not event.is_set():
            self.tick()


@contextlib.contextmanager
def basic():
    """A basic, pip-style spinner"""
    chars = ('—', '\\', '|', '/', '—', '\\', '|', '/')
    prints = [printers.back_one] * len(chars)
    spinner = Spinner(list(zip(chars, prints)))
    yield spinner
    printers.newline()


@contextlib.contextmanager
def snake():
    """Snake spinner"""
    sequence = (
        ('*', partial(printers.printf, '')),
        ('*', partial(printers.printf, '')),
        ('*', partial(printers.back, 3)),
        (' ', partial(printers.forward, 2)),
    )
    spinner = Spinner(sequence)
    yield spinner
    printers.newline()



