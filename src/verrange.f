c
c
	subroutine ver_range(inp,count,minval,maxval,mode,mni,ni,nj)
c
c This routine adds one to each point in count for each point in
c inp that is within the specified range.  If mode<0 will initialize
c count to zero.  If abs(mode).eq.2 tests for being outside range, otherwise
c for being inside of range.
c
	implicit none
	integer init,mni, ni, nj, i, j, mode
	real flag, bad
	parameter(flag = 1.e37)
	real inp(mni,nj), count(mni,nj), minval(mni,nj), maxval(mni,nj)
c
	bad = 1.e36
        if (mode.eq.-2) then

	    do 1 j=1,nj
	    do 1 i=1,ni
	      if(inp(i,j).lt.bad .and. inp(i,j).gt.maxval(i,j) .or.
     &           inp(i,j).lt.minval(i,j)) then
	         count(i,j) = 1
	      else
	         count(i,j) = 0
	      endif
1	    continue

        else if (mode.eq.2) then

	    do 2 j=1,nj
	    do 2 i=1,ni
              if (inp(i,j).lt.bad .and. inp(i,j).gt.maxval(i,j) .or.
     &            inp(i,j).lt.minval(i,j))
     &            count(i,j) = count(i,j) + 1
2	    continue

        else if (mode.lt.0) then

	    do 3 j=1,nj
	    do 3 i=1,ni
	      if(inp(i,j).le.maxval(i,j) .and. 
     &           inp(i,j).ge.minval(i,j)) then
	         count(i,j) = 1
	      else
	         count(i,j) = 0
	      endif
3	    continue

        else

	    do 4 j=1,nj
	    do 4 i=1,ni
	      if(inp(i,j).le.maxval(i,j) .and. 
     &           inp(i,j).ge.minval(i,j))
     &           count(i,j) = count(i,j) + 1
4	    continue

        endif
c
	return
	end
