"""
======
aoslib
======

aoslib is a Python library of standard atmospheric and oceanic sciences
calculation routines.  It exists mainly so we're all not writing our
own routines to calculate potential temperature, isentropic potential
vorticity, etc.
"""

import _aoslib


def calctd(t, rh, **kwargs):
    """
    Calculate dewpoint from temperature and relative humidity.

    Parameters
    ----------
    t : array_like, 2D
        Temperatures in Kelvin.
    rh : array_like, 2D
        Relative humidities (0. - 100.).
    ni : int, optional
        Number of rows to calculate dewpoint for, default is all rows.

    Returns
    -------
    td : array, 2D
        Dewpoints in Kelvin. Will have same shape as t.

    Notes
    -----
    No quality control is peformed in this routine.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calctd([[300.]], [[50.]])
    array([[ 288.70455933]], dtype=float32)

    """
    return _aoslib.calctd(t, rh, **kwargs)
