""" Unit tests for aoslib.py """

import numpy as np
from numpy.testing import assert_array_equal

import aoslib


def test_calctd():
    t = [[300., 299.], [199., 200.], [99, 100.]]
    rh = [[50.0, 50.0], [50.0, 50.0], [50., 50.]]
    three_rows = np.array([[288.70455933, 287.78875732],
                           [194.34051514, 195.29127502],
                           [97.8838501, 98.86090851]], dtype='float32')
    two_rows = np.array([[288.70455933, 287.78875732],
                         [194.34051514, 195.29127502],
                         [0., 0.]], dtype='float32')
    one_row = np.array([[288.70455933,  287.78875732],
                        [0., 0.],
                        [0., 0.]], dtype='float32')
    assert_array_equal(aoslib.calctd(t, rh), three_rows)
    assert_array_equal(aoslib.calctd(t, rh, ni=3), three_rows)
    assert_array_equal(aoslib.calctd(t, rh, ni=2), two_rows)
    assert_array_equal(aoslib.calctd(t, rh, ni=1), one_row)
