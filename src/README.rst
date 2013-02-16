==========
aoslib src
==========

Currently, this directory contains Fortran and C source code files sent
to Johnny Lin by Thomas LeFebvre at NOAA.  The code are meteorological
routines developed by the Global Systems Division of the Earth System
Research Laboratory of NOAA and are part of AWIPS I.


Building the aoslib library
===========================

aoslib is built using f2py:

f2py -c aoslib.pyf --f77flags="-fno-range-check"                    \
addaray.f        dgeocomps.f           meanomega.f    smooth.f      \
addbycnst.f      divaray.f             mixrat.f       solax.f       \
alt2press.f      dmixr.f               mslp2thkns.f   spechum2.f    \
avwind.f         dotvectors.f          multaray.f     spechum.f     \
BulkRichNo.f     dzdlnp.f              multbycnst.f   subaray.f     \
calccondprdef.f  eqlev.f               mxtp.f         sunfuncs.f    \
calccondpr.f     eqp.f                 nadgdt.f       sweat.f       \
calcdpd.f        esat.f                natlog.f       sweatidx.f    \
calcli.f         exparay.f             negarea.f      tdofesat.f    \
calcpv.f         fndiverg.f                           temp2theta.f  \
calcrh2.f        forecast.f            posarea.f      theta2temp.f  \
calcrh.f         fortconbuf.f          pottemp.f      thetawa.f     \
calctd2.f        frontogen.f           powercalc.f    totals.f      \
calctd.f         frzlev.f              press2alt.f    tplcl.f       \
calcthetae2.f    fsdiverg.f            presstable.f   tpzlcl.f      \
calcthetae.f     g2gkinematics.f       pseudolift.f   tsoar.f       \
calctv2.f        gusts.f               ptozsa.f       tv2temp.f     \
calctv.f         hailsiz.f             pvadv.f        uvcomp.f      \
calctw.f         helicity.f            pvalue.f       verpts.f      \
cclpar.f         hgt2pres.f            pvpres.f       verrange.f    \
cgp.f            interp1.f             qdiverg.f      virttemp.f    \
comp_by.f        intpos.f              qvector.f      virtualt.f    \
constant.f       IntrinsicFunctions.f  radiation.f    vp.f          \
crossvectors.f   isenstable.f          radrtns.f      vvel.f        \
ctop.f           koffset.f             rang2d.f                     \
cv_date2jul.f    lapserate.f           replinrange.f  winddir.f     \
cvgust.f         lclpar.f              rhbar.f        windspeed.f   \
ddff.f           lfcpar.f              rotvectors.f   wndrho.f      \
deftrk.f         liftedp.f             setqsmooth.f   ztopsa.f      \
density.f        lintrans.f            slfront.f                    \
derivative.f     matsln.f              slqdiv.f                     \
derived_icing.f  maxmin.f              slqvect.f                    \
adiabatic_te.c  interp.c  temp_mixratio.c  temp_of_te.c


Recreating the f2py signature file
==================================

The f2py signature file can be recreated using the following command

f2py -m _aoslib -h aoslib.pyf                                       \
addaray.f        dgeocomps.f           meanomega.f    smooth.f      \
addbycnst.f      divaray.f             mixrat.f                     \
alt2press.f      dmixr.f               mslp2thkns.f   spechum2.f    \
avwind.f         dotvectors.f          multaray.f     spechum.f     \
BulkRichNo.f     dzdlnp.f              multbycnst.f   subaray.f     \
calccondprdef.f  eqlev.f                              sunfuncs.f    \
calccondpr.f     eqp.f                 nadgdt.f       sweat.f       \
calcdpd.f        esat.f                natlog.f       sweatidx.f    \
calcli.f         exparay.f             negarea.f      tdofesat.f    \
calcpv.f         fndiverg.f                           temp2theta.f  \
calcrh2.f                              posarea.f      theta2temp.f  \
calcrh.f         fortconbuf.f          pottemp.f      thetawa.f     \
calctd2.f        frontogen.f           powercalc.f    totals.f      \
calctd.f         frzlev.f              press2alt.f    tplcl.f       \
calcthetae2.f    fsdiverg.f            presstable.f   tpzlcl.f      \
calcthetae.f     g2gkinematics.f       pseudolift.f   tsoar.f       \
calctv2.f        gusts.f               ptozsa.f       tv2temp.f     \
calctv.f         hailsiz.f             pvadv.f        uvcomp.f      \
calctw.f         helicity.f            pvalue.f       verpts.f      \
cclpar.f         hgt2pres.f            pvpres.f       verrange.f    \
cgp.f            interp1.f             qdiverg.f      virttemp.f    \
comp_by.f        intpos.f              qvector.f      virtualt.f    \
constant.f       IntrinsicFunctions.f  radiation.f    vp.f          \
crossvectors.f   isenstable.f          radrtns.f      vvel.f        \
ctop.f           koffset.f             rang2d.f                     \
cv_date2jul.f    lapserate.f           replinrange.f  winddir.f     \
cvgust.f         lclpar.f                             windspeed.f   \
ddff.f           lfcpar.f              rotvectors.f   wndrho.f      \
deftrk.f         liftedp.f             setqsmooth.f   ztopsa.f      \
density.f        lintrans.f            slfront.f                    \
derivative.f     matsln.f              slqdiv.f                     \
derived_icing.f  maxmin.f              slqvect.f


The signatures for the routines in `forecast.f`, `mxtp.f`, `rhbar.f`, and 
`solax.f` were manually created and must be added.  Copy and paste the text in
the manual_additions.pyf file into the aoslib.pyf file before the 
`end interface` line.

Notes and To Do
===============

The routines in the files `parcel.f` and `wbzero.f` are not included in the
library as there are missing external routines (tsa, ept, tv, tmr, o, tda).

The routines in the three .c files (`adiabatic_te.c`, `temp_mixratio.c` and
`temp_of_te.c`) and not wrapped.  Signatures will need to be created and added
to the aoslib.pyf file by hand.

The following files were added from the `cartographic_data.tar.gz` package of
the WRF climate model, available at http://wrf-model.org/gui/map/.  Licensing
issues of these file should be detemined.  
`ExtFtn.h`
`IntrinsicFunctions.f`
`IntrinsicFunctions.inc`
`meteoLib.h`

Minor changes were made to the soure code in the following files:
`comp_by.f` : jint function replaced with int
`fortconbuf.f` : .xor. replaced by .neqv.
`pvadv.f` : call to pv replaced with call to calcpv
`tsoar.f` : TYPE changed to PRINT and `d` removed from first column in 12
            locations 
`adiabatic_te.c` : adiabatic_te_ function added to solve name mangling issue
`temp_mixratio.c` : Name mangling issues solved.
`temp_of_te.c` : Name mangling and non-static array.
`meteroLib.h` : Commented out C definition which are not included.
Verify that these changes are required and correct.

The flag --fno-range-check is required to compile the file `fortconbuf.f`, this
should be investigated.

The signature in `aoslib.py` should be modified to correctly identify
input/output parameter, intent, etc.
>>>>>>> Updated README.rst
