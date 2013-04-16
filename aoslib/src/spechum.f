c
c
	subroutine spechum(p,t,rh,mni,ni,nj,q)
c
c..............................................................................
c
c	Routine to calculate specific humidity from the pressure, 
c	temperature, and relative humidity.
c
c	Changes:
c		P.A. Stamus	09-05-89	Original (based on Baker's)
c				09-20-89	Add implicit none.
c               J. Ramer        05-02-90        Increased algorithm speed. 
c
c	Inputs/Outputs:
c
c	   Variable     Var Type     I/O   Description
c	  ----------   ----------   ----- -------------
c	   p               RA         I    Pressure (mb)
c	   t               RA         I    Temperature (K)
c	   rh              RA         I    Relative humidity [range: 0. - 100.]
c	   mni             I          I    First dimension of input array.
c	   ni,nj           I          I    Grid dimensions in i,j.
c	   q               RA         O    Specific Humidity (g/kg).
c	
c	
c	User Notes:
c
c	1.  No quality control is performed in this routine.
c
c..............................................................................
c
	implicit none
	integer mni, ni, nj, i, j
	real p(mni,nj), t(mni,nj), rh(mni,nj)
	real q(mni,nj)
        real k,eee
        real flg,flag
        Data flg,flag/99998.0,1e37/

        Do 10 j=1,nj
        Do 10 i=1,ni
        If (p(i,j).gt.flg .or. t(i,j).gt.flg .or. rh(i,j).gt.flg) then
            q(i,j)=flag
        Else
            k=t(i,j)
            eee=rh(i,j)*exp(28.48859-0.0091379024*k-6106.396/k)
            q(i,j)=eee/(p(i,j)-0.00060771703*eee)
        End If
10      Continue

	return
	end
