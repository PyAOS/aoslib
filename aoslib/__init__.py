"""
======
aoslib
======

aoslib is a Python library of standard atmospheric and oceanic sciences
calculation routines.  It exists mainly so we're all not writing our
own routines to calculate potential temperature, isentropic potential
vorticity, etc.
"""

from .version import git_revision as __git_revision__
from .version import version as __version__

from awips import *
