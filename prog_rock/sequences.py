"""
sequences module for prog_rock
"""

# Standard library imports
from __future__ import (
    absolute_import, division, print_function, unicode_literals
)
import logging

# Third party imports

# Local imports


log = logging.getLogger(__name__)


class Spinners(object):
    """Spinners collection

    Spinners are designed to be printed, one on top of the other,
    in the specified order, indefinitely.
    """
    basic = ('—', '\\', '|', '/', '—', '\\', '|', '/')
    left_elevator = ('˥', '˦', '˧', '˨', '˩', '˨', '˧', '˦')
    corners = ('˹', '˺', '˼', '˻')
    pulsing_circle = ('҈', '۞', '۝', '۞')
    blinking_circle = ('҈', '۞')
    pulsing_circle_2 = ('࿀', '࿁')
    triangle_with_circles = ('ᐄ', 'ᐏ', 'ᐄ', 'ᐎ')
    spinning_arrowhead = ('˂', '˄', '˃', '˅')
    chasing_arrowhead = ('ˆ', 'ˇ', '˯', '˰')
    rocking_middle_bar = ('ᚾ', 'ᛅ')
    wavy_arms = ('ᚾ', 'ᛉ', 'ᛅ', 'ᛉ')
    top_bottom_arcs = ('⁀', '⁐', '‿', '⁐')
    circling_arrows = ('↱', '↴', '↲')
    pulsing_arrow = ('←', '↔', '→', '↔')
    chasing_dots = ('⠁', '⠈', '⠐', '⠠', '⢀', '⡀', '⠄', '⠂')
    accumulating_dots = (
        '⠁', '⠉', '⠙', '⠹', '⢹', '⣹', '⣽', '⣿', '⣾', '⣶', '⣦', '⣆', '⡆',
        '⠆', '⠂'
    )
    dot_elevator = ('⠉', '⠒', '⠤', '⣀', '⠤', '⠒')
    right_elevator = ('꜒', '꜓', '꜔', '꜕', '꜖', '꜕', '꜔', '꜓')
    right_dot_elevator = ('꜍', '꜎', '꜏', '꜐', '꜑', '꜐', '꜏', '꜎')
