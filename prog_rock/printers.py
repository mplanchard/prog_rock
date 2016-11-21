"""
printers module for prog_rock
"""

# Standard library imports
import logging
import sys

# Third party imports

# Local imports


log = logging.getLogger(__name__)


def printf(text):
    """

    :param text:
    :return:
    """
    sys.stdout.write(text)
    sys.stdout.flush()


def back_one():
    """Move the cursor back one space"""
    printf('\033[1D')


def back(spaces):
    """Move the cursor back spaces"""
    printf('\033[{0}D'.format(spaces))


def forward_one():
    """Move the cursor forward one space"""
    printf('\033[1C')


def forward(spaces):
    """Move the cursor forward spaces"""
    printf('\033[{0}C'.format(spaces))


def to_column(column):
    """Move the cursor to the specified column"""
    printf('\033[{0}G'.format(column))


def hide_cursor():
    """Hide the block cursor"""
    printf('\033[?25l')


def show_cursor():
    """Hide the block cursor"""
    printf('\033[?25h')


def newline():
    """Print a newline character"""
    printf('\n')
