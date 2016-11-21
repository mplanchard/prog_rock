"""
base.py module for prog_rock
"""

# Standard library imports
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import logging
import threading

# Third party imports

# Local imports


log = logging.getLogger(__name__)


class IndicatorBase(object):
    """A base class for progress indicators"""
    def __init__(self, target):
        self._target = target
        self._event = threading.Event()
        self._thread = threading.Thread(
            self._target,
            kwargs={'event': self._event}
        )

    def __enter__(self):
        self._thread.start()

    def __exit__(self):
        self._event.set()
        self._thread.join(2)
        if self._thread.is_alive():
            # TODO: better handling here
            raise RuntimeError
