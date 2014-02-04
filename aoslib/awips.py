"""
Python front end to routines in AWIPS I
"""

import _awips

def richno(ht,hw,uw,vw,rho,buoy):
    """
    Calculate Bulk Richardson number from wind components and buoyancy.
    
    Parameters
    ----------
    ht : array_like, 1D
          heights of buoyancy reports
    hw : array_like, 1D
          heights of wind reports
    vw, uw : array_like, 1D
          u and v components of wind speed (m/s).
    rho : array like, 1D
          Air density at each sounding level (kg/m**3)
    bouy : array like, 1D
          Positive buoyant energy (J/kg)
    
    Returns
    -------
    richno : real 
        Dimensionless bulk Richardson number.
    """
    return _awips.richno(ht,hw,uw,vw,rho,buoy)
           
          
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
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calctd([[300.]], [[50.]])
    array([[ 288.70455933]], dtype=float32)

    """
    return _awips.calctd(t, rh, **kwargs)


def calctd2(p, t, q, **kwargs):
    """
    Calculate dewpoint from pressure, temperature, and specific humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (Kelvin).
    q : array_like, 2D
        Specific humidity (g/Kg).
    ni : int, optional
        Number of rows to calculate dewpoint for, default is all rows.

    Returns
    -------
    td : array, 2D
        Dewpoints in Kelvin. Will have same shape as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> round(aoslib.calctd2([[1013.25]], [[296.15]], [[8.80486]]), 2)
    285.42

    """
    return _awips.calctd2(p, t, q, **kwargs)


def calccondpr(p, t, rh, **kwargs):
    """
    Calculate condensation pressure from the pressure, temperature, and
    relative humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (Kelvin).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    ni : int, optional
        Number of rows to calculate condensation pressure for, default is all
        rows.

    Returns
    -------
    q : array, 2D
        Condensation pressure (mb). Will have same shape as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calccondpr([[1013.25]], [[296.15]], [[85.]])
    array([[ 974.52386475]], dtype=float32)

    """
    return _awips.calccondpr(p, t, rh, **kwargs)


def calccondprdef(p, t, rh, **kwargs):
    """
    Calculate condensation pressure deficit from the pressure, temperature,
    and relative humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (Kelvin).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    ni : int, optional
        Number of rows to calculate condensation pressure for, default is all
        rows.

    Returns
    -------
    q : array, 2D
        Condensation pressure deficit (mb). Will have same shape as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calccondprdef([[1013.25]], [[296.15]], [[85.]])
    array([[ 38.72613525]], dtype=float32)

    """
    return _awips.calccondprdef(p, t, rh, **kwargs)


def alt2press(alt, z, **kwargs):
    """
    Calculate pressure from elevation and altimeter setting.

    Parameters
    ----------
    alt : array_like, 2D
        Altimeter setting (mb?).
    z : array_like, 2D
        Elevation  (m).
    ni : int, optional
        Number of rows to calculate pressure for, default is all rows.

    Returns
    -------
    p : array, 2D
        Pressure (mb). Will have same shape as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> round(aoslib.alt2press([[900.]], [[2000.]]), 1)
    706.1

    """
    return _awips.alt2press(alt, z, **kwargs)


def calcli(p, t, rh, t5, **kwargs):
    """
    Calculate lifted index from pressure, temperature, relative humidity,
    and 500mb (normally) temperature.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (Kelvin).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    t5 : array_like, 2D
        Temperature at 500 mb (or as given by p5 if specified) (Kelvin).
    p5 : real, optional
        Upper pressure, normally 500mb.
    ni : int, optional
        Number of rows to calculate condensation pressure for, default is all
        rows.

    Returns
    -------
    li : array, 2D
        Lifted index (C). Will have same shape as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calcli([[950.25]], [[296.15]], [[85.]], [[265.]])
    array([[-4.64505005]], dtype=float32)

    """
    return _awips.calcli(p, t, rh, t5, **kwargs)


def calcpv(p_up, p_low, th_up, th_low, u_up, v_up, u_low, v_low, dx, dy,
           coriolis, **kwargs):
    """
    Calculate isentropic potential vorticity through a layer.

    Parameters
    ----------
    p_up : array_like, 2D
        Pressure on upper isentrope (mb).
    p_low : array_like, 2D
        Pressure on lower isentrope (mb).
    th_up : real, 2D
        Upper isentrope - Theta (K).
    th_low : real, 2D
        Lower isentrope - Theta (K).
    u_up : array_like, 2D
        U-component of wind on upper isentrope (m/s).
    v_up : array_like, 2D
        V-component of wind on upper isentrope (m/s).
    u_low : array_like, 2D
        U-component of wind on lower isentrope (m/s).
    v_low : array_like, 2D
        V-component of wind on lower isentrope (m/s).
    dx : array_like, 2D
        Grid interval in x direction (m).
    dy : array_like, 2D
        Grid interval in y direction (m).
    coriolis : array_like, 2D
        Coriolis parameter (1/s).
    ni : int, optional
        Number of rows to calculate potential vorticity for, default is all
        rows.

    Returns
    -------
    pvort : array, 2D
        Potential vorticity (K/mb/s). Will have same shape as p.

    Notes
    -----
    1) Minimum number of elements in each dimension is 3.
    2) No quality control is peformed in this routine.
    3) Values > 1.e6 - 2 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    TODO

    """
    return _awips.calcpv(p_up, p_low, th_up, th_low, u_up, v_up, u_low, v_low,
                         dx, dy, coriolis, **kwargs)


def calcdpd(t, rh, **kwargs):
    """
    Calculate dewpoint depression from temperature and relative humidity.

    Parameters
    ----------
    t : array_like, 2D
        Temperatures in Kelvin.
    rh : array_like, 2D
        Relative humidities (0. - 100.).
    ni : int, optional
        Number of rows to calculate dewpoint depression for, default is all
        rows.

    Returns
    -------
    dpd : array, 2D
        Dewpoint depression in Celcius. Will have same shape as t.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calcdpd([[300.]], [[50.]])
    array([[ 11.29544067]], dtype=float32)

    """
    return _awips.calcdpd(t, rh, **kwargs)


def calcrh(t, td, **kwargs):
    """
    Calculate relative humidity from temperature and dewpoint.

    Parameters
    ----------
    t : array_like, 2D
        Temperature  (K or C).
    td : array_like, 2D
        Dewpoint (K or C -- must be same as t).
    ni : int, optional
        Number of rows to calculate relative humidity for, default is all rows.

    Returns
    -------
    rh : array, 2D
        Relative humidity (range: 0 -- 100)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calcrh([[300.]], [[290]])
    array([[ 54.30759811]], dtype=float32)

    """
    return _awips.calcrh(t, td, **kwargs)


def calcrh2(p, t, q, **kwargs):
    """
    Calculate relative humidity from pressure, temperature, and specific
    humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (Kelvin).
    q : array_like, 2D
        Specific humidity (g/Kg).
    ni : int, optional
        Number of rows to calculate relative humidity for, default is all rows.

    Returns
    -------
    rh : array, 2D
        Relative humidity (range: 0 -- 100)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calcrh2([[1013.25]], [[296.15]], [[8.667]])
    array([[ 50.00162125]], dtype=float32)

    """
    return _awips.calcrh2(p, t, q, **kwargs)


def calcthetae(p, t, rh, **kwargs):
    """
    Calculate equivalent potential temperature from the pressure, temperature,
    and relative humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (K).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    ni : int, optional
        Number of rows to calculate potential temperature for, default is all
        rows.

    Returns
    -------
    q : array, 2D
        Theta E (Equivalent potential temperature) (K). Will have same shape
        as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calcthetae([[1013.25]], [[296.15]], [[85.]])
    array([[ 336.05654907]], dtype=float32)

    """
    return _awips.calcthetae(p, t, rh, **kwargs)


def calcthetae2(p, t, td, **kwargs):
    """
    Calculate equivalent potential temperature from the pressure,
    temperature, and dewpoint.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (C or K).
    td : array_like, 2D
        Dewpoint (C or K -- must be the same as t)
    ni : int, optional
        Number of rows to calculate potential temperature for, default is all
        rows.

    Returns
    -------
    q : array, 2D
        Theta E (Equivalent potential temperature) (K). Will have same shape
        as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calcthetae2([[1013.25]], [[296.15]], [[285.7]])
    array([[ 319.97634888]], dtype=float32)

    """
    return _awips.calcthetae2(p, t, td, **kwargs)


def calctv(p, t, rh, **kwargs):
    """
    Calculate virtual temperature from the pressure, temperature, and
    relative humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (K).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    ni : int, optional
        Number of rows to calculate virtual temperature for, default is all
        rows.

    Returns
    -------
    tv : array, 2D
        Virtual temperature (K). Will have same shape as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calctv([[1013.25]], [[296.15]], [[85.]])
    array([[ 298.81143188]], dtype=float32)

    """
    return _awips.calctv(p, t, rh, **kwargs)


def calctv2(t, q, **kwargs):
    """
    Calculate virtual temperature from  temperature and specific humidity.

    Parameters
    ----------
    t : array_like, 2D
        Temperature (Kelvin).
    q : array_like, 2D
        Specific humidity (g/Kg).
    ni : int, optional
        Number of rows to calculate virtual temperature for, default is all
        rows.

    Returns
    -------
    tv : array, 2D
        Virtual temperature (K)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with falg value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calctv2([[296.15]], [[8.80486]])
    array([[ 297.73538208]], dtype=float32)

    """
    return _awips.calctv2(t, q, **kwargs)


def calctw(p, t, rh, **kwargs):
    """
    Calculate wet-bulb temperature from pressure, temperature, and relative
    humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (K).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    ni : int, optional
        Number of rows to calculate wet-bulb temperature for, default is all
        rows.

    Returns
    -------
    tw : array, 2D
        Web-bulb temperature (K). Will have same shape as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.calctw([[1013.25]], [[296.15]], [[85.]])
    array([[ 294.28710938]], dtype=float32)

    """
    return _awips.calctw(p, t, rh, **kwargs)


def cclpar(mix, p, ht, t, **kwargs):
    """
    Calculate pressure, height, and temperature of the convective condensation
    level (CCL) from a sounding.

    Parameters
    ----------
    mix : real
        Mixing ratio used to intersect the sounding (g/kg).
    p : array_like, 1D
        Sounding pressures (mb).
    ht : array_like, 1D
        Sounding heights (m above sea level)
    t : array_like, 1D
        Sounding temperatures (K).

    Returns
    -------
    pccl : real
        Pressure of the convective condensation level (mb).
    tccl : real
        Temperature of the convective condensation level (K).
    hccl : real
        Height of the convective condensation level (m above sea level).
    Notes
    -----
    1) The low level mean mixing ratio is input to this routine...
       computed outside.
    2) On days with a strong low level inversion, the convective
       temperature may seem low because the strict definition is
       used in the computation (i.e., where the low level mixing
       ratio line first intersects the sounding).
    3) Return values will contain flag value 99999. if no CCL is found.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.cclpar(.01,[830,700,530],[1707, 3169,5453],[298, 290.35,269.])
    (608.359375, 279.5761413574219, 4320.958984375)
    """
    return _awips.cclpar(mix, p, ht, t, **kwargs)


def cgp(tempip, dwptip, presip, thetawip, toppres, deltap, **kwargs):
    """
    Calculate convective gust potential based on Western Region Technical
    Attachment 76-??.

    Parameters
    ----------
    tempip: array_like, 1D (up to 400 elements)
        Temperature on the uniform pressure grid (K)
    dwptip : array_like, 1D (up to 400 elements)
        Dew point temperature on the uniform pressure grid (K)
    presip : array_like, 1D (up to 400 elements)
        Pressure on the uniform pressure grid (mb)
    thetawip : array_like, 1D (up to 400 elements)
        Wet bulb potential temperature on the uniform pressure grid (K)
    sfcpres : real
        Index of the surface pressure on the uniform pressure grid
    toppres : real
        Index of the last pressure on the uniform pressure grid
    iw : int
        >0 for mixing ratio with respect to water
        <0 for mixing ratio with respect to ice
    deltap : real
        Pressure increment of the uniform pressure grid (mb)

    Returns
    -------
    cgp : int
        Convective gust potential (1, 2, 3, 4)

    Examples (todo)
    --------
    >>> import aoslib

    """
    return _awips.cgp(tempip, dwptip, presip, thetawip, toppres, deltap,
                      **kwargs)


def derived_icing(t, rh, **kwargs):
    """
    Calculate derived icing value from temperature and relative humidity

    Parameters
    ----------
    t : array_like, 2D
        Temperature (K).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    ni : int, optional
        Number of rows to calculate derived icing for, default is all rows.

    Returns
    -------
    icg : array, 2D
        Derived icing value (non-dim)

    Notes
    -----
    Input values greater than (1.e6 - 2) are replaced on output with the flag
    value 1.e37

    Examples
    --------
    >>> import aoslib
    >>> aoslib.derived_icing([[267.15]], [[85.]])
    array([[ 3.33333325]], dtype=float32)
    """
    return _awips.derived_icing(t, rh, **kwargs)


def hgt2pres(z, **kwargs):
    """
    Calculate pressure from height based on a standard atmosphere.

    Parameters
    ----------
    z : array_like, 2D
        Height (m)
    ni : int, optional
        Number of rows to calculate pressure for, default is all rows.

    Returns
    -------
    p : array, 2D
        Pressure (mb).

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.hgt2pres([[3000]])
    array([[ 700.90557861]], dtype=float32)

    """
    return _awips.hgt2pres(z, **kwargs)


def mixrat(p, t, rh, **kwargs):
    """
    Calculate mixing ratio from the pressure, temperature, and relative
    humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (K).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    ni : int, optional
        Number of rows to calculate mixing ratio for, default is all rows.

    Returns
    -------
    q  : array, 2D
        Mixing ratio (g/kg)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.mixrat([[1013.25]], [[296.15]], [[85.]])
    array([[ 15.00989723]], dtype=float32)

    """
    return _awips.mixrat(p, t, rh, **kwargs)


def mslp2thkns(mslp, hgt, **kwargs):
    """
    Estimate 1000 to 500 mb layer thickness from 500 mb height and mean sea
    level pressure

    Parameters
    ----------
    mslp : array_like, 2D
        Mean sea level pressure (mb).
    hgt : array_like, 2D
        Height of 500 mb level (m)
    ni : int, optional
        Number of rows to estimate thickness for, default is all rows.

    Returns
    -------
    thkns  : array, 2D
        Thickness of 1000 to 500 layer (m)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.mslp2thkns([[1013.25]],[[5570]])
    array([[ 5459.20117188]], dtype=float32)

    """
    return _awips.mslp2thkns(mslp, hgt, **kwargs)


def press2alt(p, z, **kwargs):
    """
    Calculate altimeter setting from pressure and elevation

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    z : array_like, 2D
        Elevation (m)
    ni : int, optional
        Number of rows to calculate altimeter setting for, default is all rows.

    Returns
    -------
    alt  : array, 2D
        Altimeter setting (mb)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.press2alt([[800]], [[5000]])
    array([[ 1500.59912109]], dtype=float32)
    """
    return _awips.press2alt(p, z, **kwargs)


def ptozsa(p, **kwargs):
    """
    Convert a pressure into height in a standard atmosphere

    Parameters
    ----------
    p : real
        Pressure (mb).

    Returns
    -------
    z  : real
        Height in a standard atmosphere (m)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) A value > 99998.0 or < 1.0 in the input
       is replaced with flag value 1.e37 in the return value.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.ptozsa([800])
    1947.533203125
    """
    return _awips.ptozsa(p, **kwargs)


def slfront(z, t, p, dx, dy, coriolis,  **kwargs):
    """
    Calculate the QG frontogenesis function on a single level using just that
    level's data.

    Parameters
    ----------
    z : array_like, 2D
        Height field for the level (m).
    t : array_like, 2D
        Temperature field for the level (K).
    p : real
        Pressure of level (mb).
    dx : array_like, 2D
        Grid interval in x (m)
    dy : array_like, 2D
        Grid interval in y (m)
    coriolis : array_like, 2D
        Coriolis parameter (1/s)
    ni : int, optional
        Number of rows to calculate frontogenesis function for, default is all
        rows.

    Returns
    -------
    fgen : array, 2D
        Frontogenesis function for the level (?units?)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 1.e6 -2 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.
    3) At least 3 elements in each dimension are required.
    3) Bounding elements of the output array are set to 1.e37

    Examples (3 x 3 arrays of constant values as input)
    --------
    >>> import aoslib
    >>> z = [[5000,5000,5000],[5000,5000,5000],[5000,5000,5000]]
    >>> t = [[250,250,250],[250,250,250],[250,250,250]]
    >>> p = 500
    >>> dx = dy = [[400,400,400],[400,400,400],[400,400,400]]
    >>> c = [[1e-5,1e-5,1e-5],[1e-5,1e-5,1e-5],[1e-5,1e-5,1e-5]]
    >>> aoslib.slfront(z,t,p,dx,dy,c)
    array([[  9.99999993e+36,   9.99999993e+36,   9.99999993e+36],
           [  9.99999993e+36,  -0.00000000e+00,   9.99999993e+36],
           [  9.99999993e+36,   9.99999993e+36,   9.99999993e+36]], dtype=float32)

    """
    return _awips.slfront(z, t, p, dx, dy, coriolis,  **kwargs)


def spechum(p, t, rh, **kwargs):
    """
    Calculate specific humidity from pressure, temperature, and relative
    humidity.

    Parameters
    ----------
    p : array_like, 2D
        Pressure (mb).
    t : array_like, 2D
        Temperature (K).
    rh : array_like, 2D
        Relative humidity (range 0 - 100).
    ni : int, optional
        Number of rows to calculate specific humidity for, default is all rows.

    Returns
    -------
    q : array, 2D
        Specific humidity (g/kg). Will have same shape as p.

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.spechum([[1013.25]], [[296.15]], [[85.]])
    array([[ 14.78793144]], dtype=float32)

    """
    return _awips.spechum(p, t, rh, **kwargs)


def spechum2(p, td, **kwargs):
    """
    Calculate saturation specific  humidity from dewpoint and pressure.

    Parameters
    ----------
    p : array_like, 2D
        Pressure  (mb).
    td : array_like, 2D
        Dewpoint (K).
    ni : int, optional
        Number of rows to calculate specific humidity for, default is all
        rows.

    Returns
    -------
    q : array, 2D
        Specific humidity (g/kg)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.spechum2([[1000.]], [[298.]])
    array([[ 19.75852013]], dtype=float32)

    """
    return _awips.spechum2(p, td, **kwargs)


def tv2temp(tv, q, **kwargs):
    """
    Calculate temperature from the virtual temperature and specific humidity.

    Parameters
    ----------
    tv : array_like, 2D
        Virtural temperature  (K).
    q : array_like, 2D
        Specific humidity (g/kg)
    ni : int, optional
        Number of rows to calculate temperature for, default is all rows.

    Returns
    -------
    t : array, 2D
        Temperature (K)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) Values > 99998.0 in any of the input arrays
       are replaced with flag value 1.e37 in the return array.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.tv2temp([[310.]], [[19.]])
    array([[ 306.45977783]], dtype=float32)

    """
    return _awips.tv2temp(tv, q, **kwargs)


def ztopsa(z, **kwargs):
    """
    Convert a height into pressure in a standard atmosphere

    Parameters
    ----------
    z : real
        Height (m).

    Returns
    -------
    p  : real
        Pressure in a standard atmosphere (mb)

    Notes
    -----
    1) No quality control is peformed in this routine.
    2) A value > 1.e10 in the input
       is replaced with flag value 1.e37 in the return value.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.ztopsa([[1500]])
    845.43359375

    """
    return _awips.ztopsa(z, **kwargs)


def dmixr(temp, pres, iw, **kwargs):
    """
    Calculate the water vapor mixing ratio with respect to either water or
    ice.

    Parameters
    ----------
    temp : real
        Temperature (K).
    pres : real
        Pressure (mb)
    iw : int
       > 0 for mixing ratio with respect to water
       < 0 for mixing ratio with respect to ice

    Returns
    -------
    dmixr  : real
        mixing ratio (g/kg)

    Notes
    -----
    1)  Values of physical constants from Sonntag, D. 1990:
    Important new values of the physical constants of 1986,
    vapour pressure formulations based on the ITS-90, and psychrometer
    formulae. Z. Meteorol., 40, 340-344.

    Examples
    --------
    >>> import aoslib
    >>> aoslib.dmixr(301., 1000, -1)
    31.9014892578125
    >>> aoslib.dmixr(301., 1000, 1)
    24.23381233215332

    """
    return _awips.dmixr(temp, pres, iw, **kwargs)


def dzdlnp(p, t, td, **kwargs):
    """
    Calculate the rate of change of height versus the log of pressure.

    Parameters
    ----------
    p : real
        Pressure (mb)
    t : real
        Temperature (C or K).
    td : real
        Dewpoint temperature (C or K -- must be  in same units as t)
    Returns
    -------
    dzdinp  : real
        Rate of change of height versus the log of pressure.

    Notes
    -----
    1) Values less than 100 for temperature are assumed to be Celcius degrees.
    2) If td > t, it is assumed to be missing and is replaced with the value
       t - 50

    Examples
    --------
    >>> import aoslib
    >>> aoslib.dzdlnp(1013, 301., 295.)
    8896.93359375

    """
    return _awips.dzdlnp(p, t, td, **kwargs)


def radnorm(jd, **kwargs):
    """
    Calculate normalized earth-sun distance factor (R0/R)**2

    Parameters
    ----------
    jd : int
        Julian day number

    Returns
    -------
    radnorm  : real
        Normalized earth-sun distance factor

    Examples
    --------
    >>> import aoslib
    >>> aoslib.radnorm(183)
    0.9666188955307007

    """
    return _awips.radnorm(jd, **kwargs)


def soldec(jd, **kwargs):
    """
    Calculate solar declination angle

    Parameters
    ----------
    jd : int
        Julian day number

    Returns
    -------
    soldec  : real
        Solar declination angle (radians)


    Examples
    --------
    >>> import aoslib
    >>> aoslib.soldec(183)
    0.4033815860748291

    """
    return _awips.soldec(jd, **kwargs)


def timeq(jd, **kwargs):
    """
    Calculate equation of time

    Parameters
    ----------
    jd : int
        Julian day number

    Returns
    -------
    timeq  : real
        Equation of time (radians)


    Examples
    --------
    >>> import aoslib
    >>> round(aoslib.timeq(183), 5)
    -0.01598

    """
    return _awips.timeq(jd, **kwargs)


def esat(t, **kwargs):
    """
    Calculate saturation vapor pressure as a function of temperature

    Parameters
    ----------
    t : real
        Temperature (C or K).

    Returns
    -------
    esat  : real
        Saturation vapor pressure (mb)

    Notes
    -----
    1) Values less than 100 for temperature are assumed to be Celcius degrees
    2) The flag value 1.e37 is returned for input values (after conversion to
       degrees K) < 0.0 K or > 373.15

    Examples
    --------
    >>> import aoslib

    >>> aoslib.esat(273.15)
    6.106378078460693
    >>> aoslib.esat(0)
    6.106378078460693

    """
    return _awips.esat(t,  **kwargs)


def tdofesat(es, **kwargs):
    """
    Calculate dewpoint termperature as a function of saturation vapor pressure

    Parameters
    ----------
    es : real
        Saturation vapor pressure (mb).

    Returns
    -------
    tdofesat  : real
        Dewpoint termperature (K)

    Notes
    -----
    1) The flag value 1.e37 is returned for input values < 0.0 or > 980.5386

    Examples
    --------
    >>> import aoslib
    >>> round(aoslib.tdofesat(400.), 1)
    349.4

    """
    return _awips.tdofesat(es,  **kwargs)


def pottemp(temp, dwpt, pres, iw, **kwargs):
    """
    Calculate the potential temperature based on temperature, dewpoint
    temperature, and pressure

    Parameters
    ----------
    temp: real
        Temperature (C or K)
    dwpt : real
        Dew point temperature (C or K -- must be the same units as temp)
    pres :
        Pressure (mb)
    iw : int
        >0 for mixing ratio with respect to water
        <0 for mixing ratio with respect to ice

    Returns
    -------
    pottemp : int
        Potential temperature (C or K)

    Examples
    --------
    >>> import aoslib
    >>> round(aoslib.pottemp(270,265,500,1), 2)
    328.99
    >>> round(aoslib.pottemp(30,35,700,1), 3)
    33.215

    """
    return _awips.pottemp(temp, dwpt, pres, iw, **kwargs)


def thetawa(temp, dwpt, pres, iw,  **kwargs):
    """
    Calculate the adiabatic web bulb potential temperature

    Parameters
    ----------
    temp: real
        Temperature (C or K)
    dwpt : real
        Dew point temperature (C or K -- must be the same units as temp)
    pres :
        Pressure (mb)
    iw : int
        >0 for mixing ratio with respect to water
        <0 for mixing ratio with respect to ice

    Returns
    -------
    thetawa : real
        Adiabatic wet bulb potential temperature (C or K depending on input
        units)

    Notes
    -----
    1) Values less than 100 for temperature are assumed to be Celcius degrees
    1) A flag value of -999.0 is returned if this routine fails

    Examples
    --------
    >>> import aoslib
    >>> aoslib.thetawa(270,265,500,1)
    302.6724853515625
    >>> aoslib.thetawa(30,30,700,1)
    33.21508026123047





    """
    return _awips.thetawa(temp, dwpt, pres, iw,  **kwargs)
