"""
======
aoslib
======

aoslib is a Python library of standard atmospheric and oceanic sciences
calculation routines.  It exists mainly so we're all not writing our
own routines to calculate potential temperature, isentropic potential
vorticity, etc.

The following routines are currently implemented:

     alt2press -- Calculate pressure from elevation and altimeter setting.
     calccondpr -- Calculate condensation pressure from the pressure, temperature, and relative humidity.
     calccondprdef -- Calculate condensation pressure deficit from the pressure, temperature, and relative humidity.
     calcdpd -- Calculate dewpoint depression from temperature and relative humidity.
     calcli -- Calculate lifted index from pressure, temperature, relative humidity, and 500mb (normally) temperature.
     calcpv -- Calculate isentropic potential vorticity through a layer.
     calcrh -- Calculate relative humidity from temperature and dewpoint.
     calcrh2 -- Calculate relative humidity from pressure, temperature, and specific humidity.
     calctd -- Calculate dewpoint from temperature and relative humidity.' $1
     calctd2 -- Calculate dewpoint from pressure, temperature, and specific humidity.
     calcthetae -- Calculate equivalent potential temperature from the pressure, temperature, and relative humidity.
     calcthetae2 -- Calculate equivalent potential temperature from the pressure, temperature, and dewpoint.
     calctv -- Calculate virtual temperature from the pressure, temperature, and relative humidity.
     calctv2 -- Calculate virtual temperature from  temperature and specific humidity.
     calctw -- Calculate wet-bulb temperature from pressure, temperature, and relative humidity.
     cclpar -- Calculate pressure, height, and temperature of the convective condensation level (CCL) from a sounding.
     cgp -- Calculate convective gust potential based on Western Region Technical Attachment 76-??.
     derived_icing -- Calculate derived icing value from temperature and relative humidity
     dmixr -- Calculate the water vapor mixing ratio with respect to either water or ice.
     dzdlnp -- Calculate the rate of change of height versus the log of pressure.
     esat -- Calculate saturation vapor pressure as a function of temperature
     hgt2pres -- Calculate pressure from height based on a standard atmosphere.
     mixrat -- Calculate mixing ratio from the pressure, temperature, and relative humidity.
     mslp2thkns -- Estimate 1000 to 500 mb layer thickness from 500 mb height and mean sea level pressure
     pottemp -- Calculate the potential temperature based on temperature, dewpoint temperature, and pressure
     press2alt -- Calculate altimeter setting from pressure and elevation
     ptozsa -- Convert a pressure into height in a standard atmosphere
     radnorm -- Calculate normalized earth-sun distance factor (R0/R)**2
     slfront -- Calculate the QG frontogenesis function on a single level using just that level's data.
     soldec -- Calculate solar declination angle
     spechum -- Calculate specific humidity from pressure, temperature, and relative humidity.
     spechum2 -- Calculate saturation specific  humidity from dewpoint and pressure.
     tdofesat -- Calculate dewpoint termperature as a function of saturation vapor pressure
     thetawa -- Calculate the adiabatic web bulb potential temperature
     timeq -- Calculate equation of time
     tv2temp -- Calculate temperature from the virtual temperature and specific humidity.
     ztopsa -- Convert a height into pressure in a standard atmosphere
"""

from .version import git_revision as __git_revision__
from .version import version as __version__

from awips import *
