      SUBROUTINE FRZLEV(ELEV,P,HT,T,NLVLS,PFRZ,HFRZ)
      IMPLICIT NONE

C Statement of purpose.
C ---------------------
C This routine computes the pressure and height of the freezing level in
C a sounding.
C
C History.
C --------                    
C D. Baker       01 Jul 84    Original version.
C W. Kwock       24 Jul 07    DR18962: Original algorithm was freezing
C                             level is the first point that cross 273.15K
C                             from temperature above 273.15K or else
C                             freezing level is 0.
C                             The new algorithm for freezing level is the
C                             first point that cross 273.15K.  Four scenarios
C                             could happen: 1. temperature decrease and
C                             cross 273.15K. 2. temperature increase and
C                             cross 273.15K.  3. temperature never cross
C                             the 273.15K line. 4. The first value in the 
C                             temperature series is 273.15K.
C
C Description of input and output.
C --------------------------------
C On input:
C ---------                
C ELEV        Real          Station elevation (m asl).
C P           Real Array    Sounding pressures (mb).
C HT          Real Array    Sounding heights (ft asl).
C T           Real Array    Sounding temperatures (K).
C NLVLS       Integer       Number of sounding levels passed.
C
C On output:
C ----------               
C PFRZ        Real          Pressure at the freezing level (mb).
C HFRZ        Real          Height of the freezing level (ft asl).

C---- Input arguments.

      INTEGER NLVLS
      REAL ELEV,P(NLVLS),HT(NLVLS),T(NLVLS)

C---- Output variables.

      REAL HFRZ,PFRZ

C---- Internal variables.

      INTEGER I

C---- External functions.

      REAL INTERP1

C---- Subroutine constants.

      REAL TFRZ
      PARAMETER (TFRZ=273.15)

      PFRZ=P(1)   !scenario 3: no freezing level.
      HFRZ=0.

      IF (T(1).NE.TFRZ) THEN
       DO I=2,NLVLS
        IF ((T(I).LE.TFRZ) .and. (T(I-1).GT.TFRZ) .or.  !scenario 1
     1      (T(I).GE.TFRZ) .and. (T(I-1).LT.TFRZ)) THEN  !scenario 2
         HFRZ=INTERP1(HT(I),HT(I-1),T(I),TFRZ,T(I-1))
         PFRZ=INTERP1(P(I),P(I-1),HT(I),HFRZ,HT(I-1))
         GO TO 999
        ENDIF
       END DO
      ELSE
        PFRZ=P(1)  !scenario 4: first point is freezing level.
        HFRZ=HT(1)
      END IF

C---- Exit.

999   CONTINUE
      RETURN
      END
