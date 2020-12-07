import pytest
import d4part2

def test_Byr():
    assert(d4part2.containsValidByr("byr:1937"))
    assert(d4part2.containsValidByr("byr:2002"))
    assert(not d4part2.containsValidByr("byr:2003"))

def test_Htg():
    assert(d4part2.containsValidHtg("hgt:60in"))
    assert(d4part2.containsValidHtg("hgt:190cm"))
    assert(not d4part2.containsValidHtg("hgt:190in"))
    assert(not d4part2.containsValidHtg("hgt:190"))

def test_Hcl():
    assert(d4part2.containsValidHcl("hcl:#123abc"))
    assert(not d4part2.containsValidHcl("hcl:#123abz"))
    assert(not d4part2.containsValidHcl("hcl:123abc"))

def test_Ecl():
    assert(d4part2.containsValidEcl("ecl:brn"))
    assert(not d4part2.containsValidEcl("ecl:wat"))

def test_Pid():
    assert(d4part2.containsValidPid("pid:000000001"))
    assert(d4part2.containsValidPid("pid:000000001 "))
    assert(not d4part2.containsValidPid("pid:0123456789 "))
    assert(not d4part2.containsValidPid("pid:186cm "))

    assert(not d4part2.containsValidPid("hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"))
    assert(d4part2.containsValidPid("ecl:grn pid:012533040 byr:1946"))
    assert(d4part2.containsValidPid("ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"))
    assert(not d4part2.containsValidPid("pid:3556412378 byr:2007"))