""" Unit tests for aoslib.py """

import numpy as np
from numpy.testing import assert_allclose

import aoslib

verbose = 1
ATOL = 1e-3     # default absolute tolerence


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
    if verbose:
        print aoslib.calctd(t, rh)
        print aoslib.calctd(t, rh, ni=3)
        print aoslib.calctd(t, rh, ni=2)
        print aoslib.calctd(t, rh, ni=1)

    assert_allclose(aoslib.calctd(t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctd(t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctd(t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calctd(t, rh, ni=1), one_row, atol=ATOL)


def test_calctd2():
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    t = [[300., 299.], [199., 200.], [99, 100.]]
    q = [[4., 5.], [8., 9.], [10., 15.]]

    three_rows = np.array([[273.83059692,  276.22253418],
                           [282.61352539,  285.16210938],
                           [286.52270508,  293.82730103]], dtype='float32')
    two_rows = np.array([[273.83059692,  276.22253418],
                         [282.61352539,  285.16210938],
                         [0., 0.]], dtype='float32')
    one_row = np.array([[273.83059692,  276.22253418],
                        [0., 0.],
                        [0., 0.]], dtype='float32')
    if verbose:
        print "calctd2:"
        print aoslib.calctd2(p, t, q)
        print aoslib.calctd2(p, t, q, ni=3)
        print aoslib.calctd2(p, t, q, ni=2)
        print aoslib.calctd2(p, t, q, ni=1)

    assert_allclose(aoslib.calctd2(p, t, q), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctd2(p, t, q, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctd2(p, t, q, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calctd2(p, t, q, ni=1), one_row, atol=ATOL)


def test_calccondpr():
    # p,t,rh, ni
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    t = [[300., 299.], [199., 200.], [99, 100.]]
    rh = [[50.0, 50.0], [50.0, 50.0], [50., 50.]]
    three_rows = np.array([[847.81384277, 806.09692383],
                           [841.21911621, 886.18383789],
                           [915.37445068, 972.20489502]], dtype='float32')
    two_rows = np.array([[847.81384277, 806.09692383],
                         [841.21911621, 886.18383789],
                         [0., 0.]], dtype='float32')
    one_row = np.array([[847.81384277, 806.09692383],
                        [0., 0.],
                        [0., 0.]], dtype='float32')

    if verbose:
        print "calccondpr:"
        print aoslib.calccondpr(p, t, rh)
        print aoslib.calccondpr(p, t, rh, ni=3)
        print aoslib.calccondpr(p, t, rh, ni=2)
        print aoslib.calccondpr(p, t, rh, ni=1)

    assert_allclose(aoslib.calccondpr(p, t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.calccondpr(p, t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calccondpr(p, t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calccondpr(p, t, rh, ni=1), one_row, atol=ATOL)


def test_calccondprdef():
    # p,t,rh, ni
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    t = [[300., 299.], [199., 200.], [99, 100.]]
    rh = [[50.0, 50.0], [50.0, 50.0], [50., 50.]]
    three_rows = np.array(
        [[152.18615723, 143.90307617],
         [83.78088379, 88.81616211],
         [44.62554932, 47.79510498]], dtype='float32')
    two_rows = np.array(
        [[152.18615723, 143.90307617],
         [83.78088379, 88.81616211],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[152.18615723, 143.90307617],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "calccondprdef:"
        print aoslib.calccondprdef(p, t, rh)
        print aoslib.calccondprdef(p, t, rh, ni=3)
        print aoslib.calccondprdef(p, t, rh, ni=2)
        print aoslib.calccondprdef(p, t, rh, ni=1)

    assert_allclose(aoslib.calccondprdef(p, t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.calccondprdef(p, t, rh, ni=3), three_rows,
                    atol=ATOL)
    assert_allclose(aoslib.calccondprdef(p, t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calccondprdef(p, t, rh, ni=1), one_row, atol=ATOL)


def test_natlog():
    # a,b,mni,ni,nj
    a = [[1, 2.718281828],[3, 7.389056099],[-1, 5.e36]]

    three_rows = np.array(
        [[0, 1],[1.0986129, 2],[1.e37,1.e37]], dtype='float32')
    two_rows = np.array(
        [[0, 1],[1.0986129, 2],[0, 0]], dtype='float32')
    one_row = np.array(
        [[0, 1],[0, 0],[0, 0]], dtype='float32')

    if verbose:
        print "natlog:"
        print aoslib.natlog(a)
        print aoslib.natlog(a,ni=3)
        print aoslib.natlog(a,ni=2)
        print aoslib.natlog(a,ni=1)

    assert_allclose(aoslib.natlog(a), three_rows, atol=ATOL)
    assert_allclose(aoslib.natlog(a,ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.natlog(a,ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.natlog(a,ni=1), one_row, atol=ATOL)


def test_alt2press():
    # alt,z, ni
    alt = [[700., 950.], [625., 675.], [760., 1020.]]
    z = [[4000., 2000.], [5000., 4500.], [4200., 300.]]

    three_rows = np.array(
        [[425.83148193, 745.324646],
         [333.20025635, 384.56192017],
         [450.40692139, 984.23858643]], dtype='float32')
    two_rows = np.array(
        [[425.83148193, 745.324646],
         [333.20025635, 384.56192017],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[425.83148193, 745.324646],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "alt2press:"
        print aoslib.alt2press(alt, z,)
        print aoslib.alt2press(alt, z, ni=2)
        print aoslib.alt2press(alt, z, ni=1)

    assert_allclose(aoslib.alt2press(alt, z), three_rows, atol=ATOL)
    assert_allclose(aoslib.alt2press(alt, z, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.alt2press(alt, z, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.alt2press(alt, z, ni=1), one_row, atol=ATOL)


def test_calcli():
    # p,t,rh, ni
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    t = np.array([[300., 299.], [199., 200.], [274., 275.]])
    rh = np.array([[85., 85.], [85., 85.], [85., 85.]])
    t5 = np.array([[273., 268.], [183., 184.], [233., 234.]])

    three_rows = np.array(
        [[0.25119019, -5.90240479],
         [16.10115051, 18.76867676],
         [-1.99632263, 1.93981934]], dtype="float32")
    two_rows = np.array(
        [[0.25119019, -5.90240479],
         [16.10115051, 18.76867676],
         [0.0, 0.0]], dtype="float32")
    one_row = np.array(
        [[0.25119019, -5.90240479],
         [0., 0.],
         [0., 0.]], dtype='float32')
    p400 = np.array(
        [[9.80133057, 3.40185547],
         [26.41972351, 28.98414612],
         [12.01100159, 15.89608765]], dtype='float32')
    p600 = np.array(
        [[-6.87252808, -12.87338257],
         [7.16751099, 9.92427063],
         [-13.42559814, -9.57519531]], dtype='float32')

    if verbose:
        print "calcli:"
        print aoslib.calcli(p, t, rh, t5)
        print aoslib.calcli(p, t, rh, t5, ni=3)
        print aoslib.calcli(p, t, rh, t5, ni=2)
        print aoslib.calcli(p, t, rh, t5, p5=400)
        print aoslib.calcli(p, t, rh, t5, p5=600)

    assert_allclose(aoslib.calcli(p, t, rh, t5), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcli(p, t, rh, t5, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcli(p, t, rh, t5, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calcli(p, t, rh, t5, ni=1), one_row, atol=ATOL)
    assert_allclose(aoslib.calcli(p, t, rh, t5, p5=400), p400, atol=ATOL)
    assert_allclose(aoslib.calcli(p, t, rh, t5, p5=600), p600, atol=ATOL)


def test_calcdpd():
    # t,rh, ni

    t = [[300., 299.], [199., 200.], [99, 100.]]
    rh = [[50.0, 50.0], [50.0, 50.0], [50., 50.]]

    three_rows = np.array(
        [[11.29544067, 11.21124268],
         [4.65948486, 4.70872498],
         [1.1161499, 1.13909149]], dtype='float32')
    two_rows = np.array(
        [[11.29544067, 11.21124268],
         [4.65948486, 4.70872498],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[11.29544067, 11.21124268],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "calcdpd:"
        print aoslib.calcdpd(t, rh)
        print aoslib.calcdpd(t, rh, ni=3)
        print aoslib.calcdpd(t, rh, ni=2)
        print aoslib.calcdpd(t, rh, ni=1)

    assert_allclose(aoslib.calcdpd(t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcdpd(t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcdpd(t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calcdpd(t, rh, ni=1), one_row, atol=ATOL)


def test_calcrh():
    # t,td, ni

    t = [[300., 299.], [199., 200.], [99, 100.]]
    td = [[295., 294.], [196., 195.], [97., 97.]]
    three_rows = three_rows = np.array(
        [[74.13318634, 73.96073914],
         [64.2583313, 47.84600067],
         [28.55054092, 15.54915142]], dtype='float32')

    two_rows = np.array(
        [[74.13318634, 73.96073914],
         [64.2583313, 47.84600067],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[74.13318634, 73.96073914],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "calcrh:"
        print aoslib.calcrh(t, td)
        print aoslib.calcrh(t, td, ni=3)
        print aoslib.calcrh(t, td, ni=2)
        print aoslib.calcrh(t, td, ni=1)

    assert_allclose(aoslib.calcrh(t, td), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcrh(t, td, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcrh(t, td, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calcrh(t, td, ni=1), one_row, atol=ATOL)


def test_calcrh2():
    p = np.array([[1000., 950.],
                  [925., 975.],
                  [890., 1050.]], dtype='float32')
    t = np.array([[300., 299.],
                  [250., 275.],
                  [274., 275.]], dtype='float32')
    q = np.array(
        [[4.0, 5.0],
         [0.322, 2.3647],
         [3.69, 3.69]], dtype='float32')

    three_rows = np.array([[18.15696907, 22.85654831],
                           [50.29288864, 53.04074097],
                           [81.11928558, 89.06261444]], dtype='float32')
    two_rows = np.array([[18.15696907, 22.85654831],
                         [50.29288864, 53.04074097],
                         [0., 0.]], dtype='float32')
    one_row = np.array([[18.15696907,  22.85654831],
                        [0., 0.],
                        [0., 0.]], dtype='float32')
    if verbose:
        print "calcrh2:"
        print aoslib.calcrh2(p, t, q)
        print aoslib.calcrh2(p, t, q, ni=3)
        print aoslib.calcrh2(p, t, q, ni=2)
        print aoslib.calcrh2(p, t, q, ni=1)

    assert_allclose(aoslib.calcrh2(p, t, q), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcrh2(p, t, q, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcrh2(p, t, q, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calcrh2(p, t, q, ni=1), one_row, atol=ATOL)


def test_calcthetae():
    # p,t,rh, ni
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    t = [[300., 299.], [199., 200.], [99, 100.]]
    rh = [[50.0, 50.0], [50.0, 50.0], [50., 50.]]

    three_rows = np.array([[331.31411743, 334.9342041],
                           [203.48953247, 201.45625305],
                           [100.16261292, 99.43524933]], dtype='float32')

    two_rows = np.array([[331.31411743, 334.9342041],
                         [203.48953247, 201.45625305],
                         [0., 0.]], dtype='float32')
    one_row = np.array([[331.31411743, 334.9342041],
                        [0., 0.],
                        [0., 0.]], dtype='float32')
    if verbose:
        print "calcthetae:"
        print aoslib.calcthetae(p, t, rh)
        print aoslib.calcthetae(p, t, rh, ni=3)
        print aoslib.calcthetae(p, t, rh, ni=2)
        print aoslib.calcthetae(p, t, rh, ni=1)

    assert_allclose(aoslib.calcthetae(p, t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcthetae(p, t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcthetae(p, t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calcthetae(p, t, rh, ni=1), one_row, atol=ATOL)


def test_calcthetae2():
    # p,t,td, ni
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    t = [[300., 299.], [199., 200.], [99, 100.]]
    td = [[295., 294.], [196., 195.], [97., 97.]]

    three_rows = np.array(
        [[346.68173218, 350.28625488],
         [203.49028015, 201.45613098],
         [100.16261292, 99.43524933]], dtype='float32')
    two_rows = np.array(
        [[346.68173218, 350.28625488],
         [203.49028015, 201.45613098],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[346.68173218, 350.28625488],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "calcthetae2:"
        print aoslib.calcthetae2(p, t, td)
        print aoslib.calcthetae2(p, t, td, ni=3)
        print aoslib.calcthetae2(p, t, td, ni=2)
        print aoslib.calcthetae2(p, t, td, ni=1)

    assert_allclose(aoslib.calcthetae2(p, t, td), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcthetae2(p, t, td, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calcthetae2(p, t, td, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calcthetae2(p, t, td, ni=1), one_row, atol=ATOL)


def test_calctv():
    # p,t,rh, ni
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    t = [[300., 299.], [199., 200.], [99, 100.]]
    rh = [[50.0, 50.0], [50.0, 50.0], [50., 50.]]
    three_rows = np.array(
        [[302.01681519, 300.99465942],
         [199.00012207, 200.00012207],
         [99., 100.]], dtype='float32')
    two_rows = np.array(
        [[302.01681519, 300.99465942],
         [199.00012207, 200.00012207],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[302.01681519, 300.99465942],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "calctv:"
        print aoslib.calctv(p, t, rh)
        print aoslib.calctv(p, t, rh, ni=3)
        print aoslib.calctv(p, t, rh, ni=2)
        print aoslib.calctv(p, t, rh, ni=1)

    assert_allclose(aoslib.calctv(p, t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctv(p, t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctv(p, t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calctv(p, t, rh, ni=1), one_row, atol=ATOL)


def test_calctv2():
    t = [[300., 299.], [199., 200.], [99, 100.]]
    q = [[4., 5.], [8., 9.], [10., 15.]]

    three_rows = np.array(
        [[300.72958374, 299.90893555],
         [199.96792603, 201.09439087],
         [99.60192108, 100.91200256]], dtype='float32')
    two_rows = np.array(
        [[300.72958374, 299.90893555],
         [199.96792603, 201.09439087],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[300.72958374, 299.90893555],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "calctv2:"
        print aoslib.calctv2(t, q)
        print aoslib.calctv2(t, q, ni=3)
        print aoslib.calctv2(t, q, ni=2)
        print aoslib.calctv2(t, q, ni=1)

    assert_allclose(aoslib.calctv2(t, q), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctv2(t, q, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctv2(t, q, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calctv2(t, q, ni=1), one_row, atol=ATOL)


def test_calctw():
    # p,t,rh, ni
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    t = [[300., 299.], [199., 200.], [99, 100.]]
    rh = [[50.0, 50.0], [50.0, 50.0], [50., 50.]]

    three_rows = np.array(
        [[292.4899292, 291.54666138],
         [198.99752808, 199.99729919],
         [99., 100.]], dtype='float32')
    two_rows = np.array(
        [[292.4899292, 291.54666138],
         [198.99752808, 199.99729919],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[292.4899292, 291.54666138],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "calctw:"
        print aoslib.calctw(p, t, rh)
        print aoslib.calctw(p, t, rh, ni=3)
        print aoslib.calctw(p, t, rh, ni=2)
        print aoslib.calctw(p, t, rh, ni=1)

    assert_allclose(aoslib.calctw(p, t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctw(p, t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.calctw(p, t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.calctw(p, t, rh, ni=1), one_row, atol=ATOL)


def test_constant():
    # a, const, ni, nj
    a = [[1000., 950.],[925., 975.],[-960., -1020.]]
    const = -3.14

    three_rows = np.array(
	[[-3.14,-3.14],
	[-3.14,-3.14],
	[-3.14, -3.14]],dtype='float32')
    two_rows = np.array(
	[[-3.14,-3.14],
	[-3.14,-3.14],
	[-960., -1020.]],dtype='float32')
    one_row = np.array(
	[[-3.14,-3.14],
	[925.,975.],
	[-960., -1020.]],dtype='float32')
    zero_rows = np.array(
        [[1000., 950.], 
        [925., 975.],
        [-960., -1020.]],dtype='float32')

    if verbose:
        print "constant:"
        print aoslib.constant(a, const)
        print aoslib.constant(a, const, ni=3)
        print aoslib.constant(a, const, ni=2)
        print aoslib.constant(a, const, ni=1)
        print aoslib.constant(a, const, ni=0)

    assert_allclose(aoslib.constant(a,const), three_rows, atol=ATOL)
    assert_allclose(aoslib.constant(a,const,ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.constant(a,const,ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.constant(a,const,ni=1), one_row, atol=ATOL)
    assert_allclose(aoslib.constant(a,const,ni=0), zero_rows, atol=ATOL)


def test_crossvectors():
    # ax, ay, bx, by
    ax = [[1000., 950.], [925., 975.], [960., 1020.]]
    ay = [[300., 299.], [199., 200.], [99, 100.]]
    bx = [[50.0, 50.0], [50.0, 50.0], [50., 50.]]
    by = [[60.0, 60.0], [60.0, 60.0], [60., 60.]]
    three_rows = np.array(
        [[45000.,  42050.],
         [45550.,  48500.],
         [52650.,  56200.]], dtype='float32')
    two_rows = np.array(
        [[45000.,  42050.],
         [45550.,  48500.],
         [    0.,      0.]], dtype='float32')
    one_row = np.array(
        [[45000.,  42050.],
         [    0.,      0.],
         [    0.,      0.]], dtype='float32')

    if verbose:
        print "crossvectors:"
        print aoslib.crossvectors(ax,ay,bx,by)
        print aoslib.crossvectors(ax,ay,bx,by, ni=3)
        print aoslib.crossvectors(ax,ay,bx,by, ni=2)
        print aoslib.crossvectors(ax,ay,bx,by, ni=1)

    assert_allclose(aoslib.crossvectors(ax,ay,bx,by), three_rows, atol=ATOL)
    assert_allclose(aoslib.crossvectors(ax,ay,bx,by, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.crossvectors(ax,ay,bx,by, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.crossvectors(ax,ay,bx,by, ni=1), one_row, atol=ATOL)


def test_ctop():
    # p,ht,vv,peqlev
    p = [7., 7., 7.]
    ht = [7., 7., 7.]
    vv = [7., 7., 7.]
    peqlev = 7
    answer = np.array(99999.)

    if verbose:
        print "ctop:"
        print aoslib.ctop(p, ht, vv, peqlev)

    assert_allclose(aoslib.ctop(p, ht, vv, peqlev), answer, atol=ATOL)


def test_derived_icing():
    # t, rh, ni
    t = [[300., 299.], [268., 274.], [258., 267.43572]]
    rh = [[50.0, 80.0], [50.0, 50.0], [60., 30.]]

    three_rows = np.array(
        [[-12.42500305, -11.92500305],
         [1., 0.57499695],
         [1.66666663, -0.33333334]], dtype='float32')
    two_rows = np.array(
        [[-12.42500305, -11.92500305],
         [1., 0.57499695],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[-12.42500305, -11.92500305],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "derived_icing:"
        print aoslib.derived_icing(t, rh)
        print aoslib.derived_icing(t, rh, ni=3)
        print aoslib.derived_icing(t, rh, ni=2)
        print aoslib.derived_icing(t, rh, ni=1)

    assert_allclose(aoslib.derived_icing(t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.derived_icing(t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.derived_icing(t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.derived_icing(t, rh, ni=1), one_row, atol=ATOL)


def test_hgt2pres():
    # z, ni
    z = [[2000., 2500.], [5000., 5500.], [7000., 8000.]]

    three_rows = np.array(
        [[794.80554199, 746.66101074],
         [539.9765625, 504.83911133],
         [410.36773682, 355.75720215]], dtype='float32')
    two_rows = np.array(
        [[794.80554199, 746.66101074],
         [539.9765625, 504.83911133],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[794.80554199, 746.66101074],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "hgt2pres:"
        print aoslib.hgt2pres(z)
        print aoslib.hgt2pres(z, ni=3)
        print aoslib.hgt2pres(z, ni=2)
        print aoslib.hgt2pres(z, ni=1)

    assert_allclose(aoslib.hgt2pres(z), three_rows, atol=ATOL)
    assert_allclose(aoslib.hgt2pres(z, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.hgt2pres(z, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.hgt2pres(z, ni=1), one_row, atol=ATOL)


def test_mixrat():
    # p,t,rh, ni
    p = np.array([[1000., 950.],
                  [925., 975.],
                  [890., 1050.]], dtype='float32')
    t = np.array([[300., 299.],
                  [250., 275.],
                  [274., 275.]], dtype='float32')
    rh = np.array([[18.15696907, 22.85654831],
                   [50.29288864, 53.04074097],
                   [81.11928558, 89.06261444]], dtype='float32')

    three_rows = np.array(
        [[4.01606226, 5.02512312],
         [0.32210353, 2.37029934],
         [3.70366383, 3.70365715]], dtype='float32')
    two_rows = np.array(
        [[4.01606226, 5.02512312],
         [0.32210353, 2.37029934],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[4.01606226, 5.02512312],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "mixrat:"
        print aoslib.mixrat(p, t, rh)
        print aoslib.mixrat(p, t, rh, ni=3)
        print aoslib.mixrat(p, t, rh, ni=2)
        print aoslib.mixrat(p, t, rh, ni=1)

    assert_allclose(aoslib.mixrat(p, t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.mixrat(p, t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.mixrat(p, t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.mixrat(p, t, rh, ni=1), one_row, atol=ATOL)


def test_mslp2thkns():
    # mslp,hgt, ni
    mslp = [[1000., 950.], [925., 975.], [960., 1020.]]
    hgt = [[4000., 2000.], [5000., 4500.], [4200., 300.]]

    three_rows = np.array(
        [[3999.99804688, 2170.61645508],
         [5676.44970703, 4682.1015625],
         [4480.56738281, 291.10598755]], dtype='float32')
    two_rows = np.array(
        [[3999.99804688, 2170.61645508],
         [5676.44970703, 4682.1015625],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[3999.99804688, 2170.61645508],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "mslp2thkns:"
        print aoslib.mslp2thkns(mslp, hgt)
        print aoslib.mslp2thkns(mslp, hgt, ni=3)
        print aoslib.mslp2thkns(mslp, hgt, ni=2)
        print aoslib.mslp2thkns(mslp, hgt, ni=1)

    assert_allclose(aoslib.mslp2thkns(mslp, hgt), three_rows, atol=ATOL)
    assert_allclose(aoslib.mslp2thkns(mslp, hgt, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.mslp2thkns(mslp, hgt, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.mslp2thkns(mslp, hgt, ni=1), one_row, atol=ATOL)


def test_press2alt():
    # p,z, ni
    p = [[1000., 950.], [925., 975.], [960., 1020.]]
    z = [[4000., 2000.], [5000., 4500.], [4200., 300.]]

    three_rows = np.array(
        [[1643.84277344, 1210.88171387],
         [1735.06774902, 1711.36291504],
         [1619.86853027, 1057.06079102]], dtype='float32')
    two_rows = np.array(
        [[1643.84277344, 1210.88171387],
         [1735.06774902, 1711.36291504],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[1643.84277344, 1210.88171387],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "press2alt:"
        print aoslib.press2alt(p, z,)
        print aoslib.press2alt(p, z, ni=3)
        print aoslib.press2alt(p, z, ni=2)
        print aoslib.press2alt(p, z, ni=1)

    assert_allclose(aoslib.press2alt(p, z,), three_rows, atol=ATOL)
    assert_allclose(aoslib.press2alt(p, z, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.press2alt(p, z, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.press2alt(p, z, ni=1), one_row, atol=ATOL)


def test_spechum():
    # p,t,rh, ni

    p = np.array([[1000., 950.],
                  [925., 975.],
                  [890., 1050.]], dtype='float32')
    t = np.array([[300., 299.],
                  [250., 275.],
                  [274., 275.]], dtype='float32')
    rh = np.array([[18.15696907, 22.85654831],
                   [50.29288864, 53.04074097],
                   [81.11928558, 89.06261444]], dtype='float32')

    three_rows = np.array(
        [[3.99999785, 4.99999762],
         [0.32199982, 2.36469412],
         [3.68999743, 3.689991]], dtype='float32')

    two_rows = np.array(
        [[3.99999785, 4.99999762],
         [0.32199982, 2.36469412],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[3.99999785, 4.99999762],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "spechum:"
        print aoslib.spechum(p, t, rh)
        print aoslib.spechum(p, t, rh, ni=3)
        print aoslib.spechum(p, t, rh, ni=2)
        print aoslib.spechum(p, t, rh, ni=1)

    assert_allclose(aoslib.spechum(p, t, rh), three_rows, atol=ATOL)
    assert_allclose(aoslib.spechum(p, t, rh, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.spechum(p, t, rh, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.spechum(p, t, rh, ni=1), one_row, atol=ATOL)


def test_spechum2():
    # p,td, ni

    p = np.array(
        [[1000., 950.],
         [925., 975.],
         [890., 1050.]], dtype='float32')
    td = np.array(
        [[273.83059692, 276.22253418],
         [242.49562073, 266.45379639],
         [271.13580322, 273.39309692]], dtype='float32')

    three_rows = np.array(
        [[3.99999404, 5.0000186],
         [0.32199925, 2.36470199],
         [3.69000816, 3.68999887]], dtype='float32')
    two_rows = np.array(
        [[3.99999404, 5.0000186],
         [0.32199925, 2.36470199],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[3.99999404, 5.0000186],
         [0., 0.],
         [0., 0.]], dtype='float32')

    if verbose:
        print "spechum2:"
        print aoslib.spechum2(p, td)
        print aoslib.spechum2(p, td, ni=3)
        print aoslib.spechum2(p, td, ni=2)
        print aoslib.spechum2(p, td, ni=1)

    assert_allclose(aoslib.spechum2(p, td), three_rows, atol=ATOL)
    assert_allclose(aoslib.spechum2(p, td, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.spechum2(p, td, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.spechum2(p, td, ni=1), one_row, atol=ATOL)


def test_tv2temp():
    # tv, q, ni
    tv = np.array([[300., 299.],
                  [250., 275.],
                  [274., 275.]], dtype='float32')
    q = np.array(
        [[3.99999785, 4.99999762],
         [0.32199982, 2.36469412],
         [3.68999743, 3.689991]], dtype='float32')

    three_rows = np.array(
        [[299.27218628, 298.09381104],
         [249.95108032, 274.60516357],
         [273.38665771, 274.38439941]], dtype='float32')

    two_rows = np.array(
        [[299.27218628, 298.09381104],
         [249.95108032, 274.60516357],
         [0., 0.]], dtype='float32')
    one_row = np.array(
        [[299.27218628, 298.09381104],
         [0., 0.],
         [0., 0.]], dtype='float32')
    if verbose:
        print "tv2temp:"
        print aoslib.tv2temp(tv, q)
        print aoslib.tv2temp(tv, q, ni=3)
        print aoslib.tv2temp(tv, q, ni=2)
        print aoslib.tv2temp(tv, q, ni=1)

    assert_allclose(aoslib.tv2temp(tv, q), three_rows, atol=ATOL)
    assert_allclose(aoslib.tv2temp(tv, q, ni=3), three_rows, atol=ATOL)
    assert_allclose(aoslib.tv2temp(tv, q, ni=2), two_rows, atol=ATOL)
    assert_allclose(aoslib.tv2temp(tv, q, ni=1), one_row, atol=ATOL)


def test_ptozsa():
    pin = np.array([800., 200., 50., 1000., 500., 700.], dtype='float32')
    zout = np.zeros_like(pin)

    test_out = np.array(
        [1947.53320312, 11777.66894531, 20567.74609375, 110.40789795,
         5571.04736328, 3010.15991211], dtype='float32')

    it = np.nditer(pin, flags=['c_index'])
    while not it.finished:
        zout[it.index] = aoslib.ptozsa(it[0])
        it.iternext()
    if verbose:
        print("ptozsa:")
        print(zout)
    assert_allclose(zout, test_out, atol=1e-8, rtol=1e-5)


def test_ztopsa():
    zin = np.array(
        [1947.53320312, 11777.66894531, 20567.74609375, 110.40789795,
         5571.04736328, 3010.15991211], dtype='float32')
    pout = np.zeros_like(zin)

    test_out = np.array(
        [799.99993896, 200.00001526, 49.99999237, 1000.00024414,
         500.00006104, 700.], dtype='float32')

    it = np.nditer(zin, flags=['c_index'])
    while not it.finished:
        pout[it.index] = aoslib.ztopsa(it[0])
        it.iternext()
    if verbose:
        print("ztopsa:")
        print(pout)
    assert_allclose(pout, test_out, atol=ATOL)


def test_dmixr():
    p = np.array([1000., 950., 925., 975., 890., 1050.], dtype='float32')
    t = np.array([300., 299., 250., 275., 274., 275.], dtype='float32')
    mrw = np.zeros_like(p)
    mri = np.zeros_like(p)
    test_mrw = np.array([22.80476761, 22.62307739, 0.64204776, 4.48768139,
                         4.5760417, 4.16498613], dtype='float32')
    test_mri = np.array([29.71182823, 29.1896553, 0.51151443, 4.56883192,
                         4.61366463, 4.24026203], dtype='float32')

    it = np.nditer(p, flags=['c_index'])
    while not it.finished:
        mrw[it.index] = aoslib.dmixr(t[it.index], p[it.index], 1)
        mri[it.index] = aoslib.dmixr(t[it.index], p[it.index], -1)
        it.iternext()
    if verbose:
        print("dmixr:")
        print(mrw)
        print(mri)
    assert_allclose(mrw, test_mrw, atol=ATOL)
    assert_allclose(mri, test_mri, atol=ATOL)


def test_dzdlnp():
    p = np.array([1000., 950., 925., 975., 960., 1020.], dtype='float32')
    t = np.array([300., 299., 199., 200., 99, 100.], dtype='float32')
    td = np.array([295., 294., 196., 195., 97., 97], dtype='float32')

    dzdlp = np.zeros_like(p)
    test_out = np.array(
        [8868.51464844, 8838.07519531, 5824.51318359, 5853.78125,
         16683.05664062, 2926.88891602], dtype='float32')

    it = np.nditer(p, flags=['c_index'])
    while not it.finished:
        dzdlp[it.index] = aoslib.dzdlnp(p[it.index], t[it.index], td[it.index])
        it.iternext()
    if verbose:
        print("dzdlnp:")
        print(dzdlp)

    assert_allclose(dzdlp, test_out, atol=ATOL)


def test_radnorm():
    jd = np.array([300, 365, 1, 182, 90, 275])
    rd = np.zeros(len(jd), dtype='float32')

    test_out = np.array([1.01283681, 1.03501987, 1.03505003, 0.96664751,
                         1.00200331, 0.99825764], dtype='float32')

    it = np.nditer(jd, flags=['c_index'])
    while not it.finished:
        rd[it.index] = aoslib.radnorm(jd[it.index])
        it.iternext()

    if verbose:
        print("radnorm:")
        print(rd)

    assert_allclose(rd, test_out, atol=ATOL)


def test_soldec():
    jd = np.array([300, 365, 1, 182, 90, 275])
    sd = np.zeros(len(jd), dtype='float32')

    test_out = np.array([-0.21854927, -0.40369907, -0.40244898, 0.40451825,
                         0.06728737, -0.05679472], dtype='float32')

    it = np.nditer(jd, flags=['c_index'])
    while not it.finished:
        sd[it.index] = aoslib.soldec(jd[it.index])
        it.iternext()

    if verbose:
        print("soldec:")
        print(sd)

    assert_allclose(sd, test_out, atol=ATOL)


def test_timeq():
    jd = np.array([300, 365, 1, 182, 90, 275])
    tq = np.zeros(len(jd), dtype='float32')

    test_out = np.array([0.07059176, -0.01070544, -0.012672, -0.01510747,
                         -0.0204956, 0.04712578], dtype='float32')

    it = np.nditer(jd, flags=['c_index'])
    while not it.finished:
        tq[it.index] = aoslib.timeq(jd[it.index])
        it.iternext()

    if verbose:
        print("timeq:")
        print(tq)

    assert_allclose(tq, test_out, rtol=1e-06)


def test_esat():
    tk = np.array([300., 299., 320., 230., 274., 275.], dtype='float32')
    tc = tk - 273.15
    satk = np.zeros_like(tk)
    satc = np.zeros_like(tk)
    test_out = np.array([35.33226013, 33.30999374, 105.02552795, 0.13663472,
                         6.49424458, 6.97839975],  dtype='float32')

    it = np.nditer(tk, flags=['c_index'])
    while not it.finished:
        satk[it.index] = aoslib.esat(tk[it.index])
        satc[it.index] = aoslib.esat(tc[it.index])
        it.iternext()

    if verbose:
        print("esat:")
        print(satk)
        print(satc)

    assert_allclose(satk, test_out, atol=ATOL)
    assert_allclose(satc, test_out, atol=ATOL)


def test_tdofesat():
    es = np.array([35.33226013, 33.30999374, 105.02552795, 0.13663472,
                   6.49424458, 6.97839975], dtype='float32')

    td = np.zeros_like(es)

    test_out = np.array([299.99993896, 299.00003052, 319.99996948,
                         230.00004578, 274., 275.], dtype='float32')

    it = np.nditer(es, flags=['c_index'])
    while not it.finished:
        td[it.index] = aoslib.tdofesat(es[it.index])
        it.iternext()

    if verbose:
        print("tdofesat:")
        print(td)

    assert_allclose(td, test_out, atol=ATOL)


def test_pottemp():
    temp = np.array([300., 274., 199., 200., 99, 100.], dtype='float32')
    dwpt = np.array([295., 265., 196., 195., 97., 97.], dtype='float32')
    pres = np.array([1000., 500., 625., 975., 960., 1020.], dtype='float32')

    ptw = np.zeros_like(temp)
    pti = np.zeros_like(temp)
    test_ptw = np.array([300., 333.86026001, 227.56678772, 201.45037842,
                         100.16015625, 99.43642426], dtype='float32')
    test_pti = np.array([300.,  333.8661499, 227.56680298, 201.45037842,
                         100.16015625, 99.43642426], dtype='float32')

    it = np.nditer(temp, flags=['c_index'])
    while not it.finished:
        ptw[it.index] = aoslib.pottemp(temp[it.index], dwpt[it.index],
                                       pres[it.index], 1)
        pti[it.index] = aoslib.pottemp(temp[it.index], dwpt[it.index],
                                       pres[it.index], -1)
        it.iternext()
    if verbose:
        print("pottemp:")
        print(ptw)
        print(pti)
    assert_allclose(ptw, test_ptw, atol=ATOL)
    assert_allclose(pti, test_pti, atol=ATOL)


def test_thetawa():
    temp = np.array([300., 274., 199., 200., 99, 30.], dtype='float32')
    dwpt = np.array([295., 265., 196., 195., 97., 27.], dtype='float32')
    pres = np.array([1000., 500., 625., 975., 960., 720.], dtype='float32')

    ptw = np.zeros_like(temp)
    pti = np.zeros_like(temp)
    test_ptw = np.array([297.34692383, 304.38040161, 227.4776001,
                        201.44902039, -999.,   32.94946289], dtype='float32')
    test_pti = np.array([297.35095215, 304.37991333, 227.4776001,
                         201.44902039, -999., 32.94946289], dtype='float32')

    it = np.nditer(temp, flags=['c_index'])
    while not it.finished:
        ptw[it.index] = aoslib.thetawa(temp[it.index], dwpt[it.index],
                                       pres[it.index], 1)
        pti[it.index] = aoslib.thetawa(temp[it.index], dwpt[it.index],
                                       pres[it.index], -1)
        it.iternext()
    if verbose:
        print("thetawa:")
        print(ptw)
        print(pti)
    assert_allclose(ptw, test_ptw, atol=ATOL)
    assert_allclose(pti, test_pti, atol=ATOL)


def test_cclpar():
    p = np.array([841.0, 700.0, 500.0, 400.0, 300.0, 250.0, 200.0, 150.0,
                  100.0, 70.00,  50.00, 30.00,  20.00], dtype='float32')
    h = np.array(
        [1542.80444336, 3010.15991211, 5571.04736328, 7181.19189453,
         9158.66503906, 10357.0205078, 11777.6689453, 13601.7753906,
         16172.7070312, 18434.2773438, 20567.7460938, 23806.7363281,
         26377.6679688], dtype='float32')
    t = np.array([296.6, 287.0, 266.9, 257.5, 242.1, 231.1, 220.7, 206.5,
                  204.5, 212.3, 216.7, 224.5, 223.3], dtype='float32')

    test_res1 = (841.0, 296.6000061035156, 1542.804443359375)
    test_res2 = (621.875, 279.8951110839844, 3910.8525390625)

    res1 = aoslib.cclpar(0.1, p, h, t)
    res2 = aoslib.cclpar(0.01, p, h, t)
    if verbose:
        print("cclpar:")
        print(res1)
        print(res2)
    assert_allclose(res1, test_res1, atol=ATOL)
    assert_allclose(res2, test_res2, atol=ATOL)


def test_add_aray():

    # simple test
    res = aoslib.add_aray([1, 2, 3], [4, 5, 6])
    assert res.shape == (3, 1)
    assert res.dtype == 'float32'
    assert_allclose(res, [[5], [7], [9]])

    # mode parameter
    assert aoslib.add_aray([1, 2, 3], [4, 5, 1.e37])[2, 0] > 9.e36
    assert aoslib.add_aray([1, 2, 3], [4, 5, 1.e37], mode=0)[2, 0] > 9.e36
    assert aoslib.add_aray([1, 2, 3], [4, 5, 1.e37], mode=1)[2, 0] == 3

    # ni parameter
    assert aoslib.add_aray([1, 2, 3], [4, 5, 6])[2, 0] == 9
    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=3)[2, 0] == 9

    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=2)[2, 0] == 0
    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=2)[1, 0] == 7

    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=1)[2, 0] == 0
    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=1)[1, 0] == 0
    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=1)[0, 0] == 5

    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=0)[2, 0] == 0
    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=0)[1, 0] == 0
    assert aoslib.add_aray([1, 2, 3], [4, 5, 6], ni=0)[0, 0] == 0


def test_add_by_cnst():

    # simple test
    a = np.ones((2, 3))
    assert np.all(aoslib.add_by_cnst(a, 2) == 3)
    assert np.all(aoslib.add_by_cnst(a, -1) == 0)
    assert np.all(aoslib.add_by_cnst(a, 10) == 11)

    # ni parameter
    a = np.ones((2, 3))
    assert np.all(aoslib.add_by_cnst(a, 2, ni=2) == 3)

    assert np.all(aoslib.add_by_cnst(a, 2, ni=1)[0] == 3)
    assert np.all(aoslib.add_by_cnst(a, 2, ni=1)[1] == 0)

    assert np.all(aoslib.add_by_cnst(a, 2, ni=0) == 0)

    # missing value
    a = np.ones((2, 3))
    a[1, 1] = 1e37
    assert aoslib.add_by_cnst(a, 2)[0, 0] == 3
    assert aoslib.add_by_cnst(a, 2)[1, 1] != 3


def test_div_aray():

    # simple test
    a = np.ones((2, 3))
    b = np.ones((2, 3)) * 2
    assert np.all(aoslib.div_aray(a, b) == 0.5)

    # ni parameter
    a = np.ones((2, 3))
    b = np.ones((2, 3)) * 2
    assert np.all(aoslib.div_aray(a, b, ni=2) == 0.5)

    assert np.all(aoslib.div_aray(a, b, ni=1)[0] == 0.5)
    assert np.all(aoslib.div_aray(a, b, ni=1)[1] == 0)

    assert np.all(aoslib.div_aray(a, b, ni=0) == 0)
