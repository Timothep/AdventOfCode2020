import pytest
import d5part1

boundsRow = [0,127]
boundsColumns = [0,7]

def test_validColumnDown():
    bounds = d5part1.getNextSubdivision([0,127], 'F')
    assert(bounds == [0,63])

def test_validColumnUp():
    bounds = d5part1.getNextSubdivision([0,127], 'B')
    assert(bounds == [64,127])

def test_validRowDown():
    bounds = d5part1.getNextSubdivision([0,7], 'L')
    assert(bounds == [0,3])

def test_validRowUp():
    bounds = d5part1.getNextSubdivision([0,7], 'R')
    assert(bounds == [4,7])

def test_getFront():
    row = d5part1.getPosition(boundsRow, "FFFFFFF")
    assert(row == 0)

def test_getBack():
    row = d5part1.getPosition(boundsRow, "BBBBBBB")
    assert(row == 127)

def test_getRow0():
    row = d5part1.getPosition(boundsRow, "FBFBBFF")
    assert(row == 44)

def test_getRow1():
    row = d5part1.getPosition(boundsRow, "BFFFBBF")
    assert(row == 70)

def test_getRow2():
    row = d5part1.getPosition(boundsRow, "FFFBBBF")
    assert(row == 14)

def test_getRow3():
    row = d5part1.getPosition(boundsRow, "BBFFBBF")
    assert(row == 102)

def test_getColumn0():
    column = d5part1.getPosition(boundsColumns, "RLR")
    assert(column == 5)

def test_getColumn1():
    column = d5part1.getPosition(boundsColumns, "RRR")
    assert(column == 7)

def test_getColumn2():
    column = d5part1.getPosition(boundsColumns, "RLL")
    assert(column == 4)

def test_getRowAndColumn():
    rowncolumn = d5part1.getRowAndColumn("FBFBBFFRLR")
    assert(rowncolumn[0] == 44)
    assert(rowncolumn[1] == 5)

def test_getId():
    assert(357 == d5part1.computeId("FBFBBFFRLR"))

#def test_findHighestSeatId():
#    assert(820 == d5part1.findHighestSeatId(["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]))