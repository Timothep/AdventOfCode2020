import pytest
import day6part1
import day6part2

def test_getUniqueCount():
    assert(3 == day6part1.getUniqueCount("abc"))

def test_intersection0():
    assert("" == day6part2.intersectionOfStrings("ab","cd"))

def test_intersection1():
    assert("a" == day6part2.intersectionOfStrings("ab","ac"))

def test_countLettersInAllElements0():
    assert(0 == day6part2.countLettersInAllElements(["ab", "cd"]))

def test_countLettersInAllElements1():
    assert(1 == day6part2.countLettersInAllElements(["ab", "ac"]))