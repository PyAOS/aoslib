C---- Given Y1 AT X1, Y3 AT X3, and X2, calculate Y2 (INTERP) AT X2.

      REAL FUNCTION INTERP1(Y1,Y3,X1,X2,X3)
      IMPLICIT NONE
      REAL Y1,Y3,X1,X2,X3
      IF (X3.EQ.X1) X1=X1-0.01
      INTERP1=Y1+((Y3-Y1)*((X2-X1)/(X3-X1)))
      RETURN
      END
