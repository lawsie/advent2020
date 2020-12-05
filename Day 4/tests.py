import re

testdata = [
    ["byr", 1920], ["byr", 1921], ["byr", 2001], ["byr", 2001],
    ["iyr", 2010], ["iyr", 2011], ["iyr", 2019], ["iyr", 2020],
    ["eyr", 2020], ["eyr", 2021], ["eyr", 2029], ["eyr", 2030],
    ["hgt", "150cm"], ["hgt", "151cm"], ["hgt", "193cm"], ["hgt", "59in"],["hgt", "60in"], ["hgt", "76in"],
    ["hcl", "#012345"], ["hcl", "#abcdef"], ["hcl", "#0a1b2c"],
    ["ecl", "amb"], ["ecl", "blu"], ["ecl", "brn"], ["ecl", "gry"], ["ecl", "grn"], ["ecl", "hzl"], ["ecl", "oth"],
    ["pid", "000000001"], ["pid", "123456789"]
]

"""
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
        """

for test in testdata:
    this_pass_valid = True
    if test[0] == "byr":
        if int(test[1]) < 1920 or int(test[1]) > 2002:
            this_pass_valid = False
    elif test[0] == "iyr":
        if int(test[1]) < 2010 or int(test[1]) > 2020:
            this_pass_valid = False
    elif test[0] == "eyr":
        if int(test[1]) < 2020 or int(test[1]) > 2030:
            this_pass_valid = False
    elif test[0] == "hgt":
        if test[1][-2:] == "cm":
            if int(test[1][:-2]) < 150 or int(test[1][:-2]) > 193:
                this_pass_valid = False
        elif test[1][-2:] == "in":
            if int(test[1][:-2]) < 59 or int(test[1][:-2]) > 76:
                this_pass_valid = False
    elif test[0] == "hcl":
        # # followed by exactly six characters 0-9 or a-f
        match = re.search("^#([0-9a-f]){6}$", test[1])
        if not match:
            this_pass_valid = False
    elif test[0] == "ecl":
        if test[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            this_pass_valid = False
    elif test[0] == "pid":
        if len(test[1]) != 9 or isinstance(test[1], int) == False:
            this_pass_valid = False
    else:
            this_pass_valid = False
    if this_pass_valid:
        print("PASS")
    else:
        print("FAIL" + str(test))

print("----------------")

faildata = [
    ["byr", 1919], ["byr", 2003],
    ["iyr", 2009], ["iyr", 2021],
    ["eyr", 2019], ["eyr", 2031], 
    ["hgt", "149cm"], ["hgt", "194cm"], ["hgt", "58in"], ["hgt", "77in"], ["hgt", "77i"],
    ["hcl", "#0123456"], ["hcl", "#abcdefg"], ["hcl", "#01234"], ["hcl", "#abcde"], ["hcl", "#0a1b2c3"], ["hcl", "#0a1b2"], 
    ["hcl", "0a1b2c3"], ["hcl", "123456"], ["hcl", "abcdef"], ["hcl", "a1b2c3#"], ["hcl", "0a#b2c3"], ["hcl", "#ABCDEF"],
    ["ecl", "bla"], ["ecl", ""],
    ["pid", "1"], ["pid", "1234567890"], ["pid", "abcdefghi"]
]

"""
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
        """

for test in faildata:
    this_pass_valid = True
    if test[0] == "byr":
        if int(test[1]) < 1920 or int(test[1]) > 2002:
            this_pass_valid = False
    elif test[0] == "iyr":
        if int(test[1]) < 2010 or int(test[1]) > 2020:
            this_pass_valid = False
    elif test[0] == "eyr":
        if int(test[1]) < 2020 or int(test[1]) > 2030:
            this_pass_valid = False
    elif test[0] == "hgt":
        if test[1][-2:] == "cm":
            if int(test[1][:-2]) < 150 or int(test[1][:-2]) > 193:
                this_pass_valid = False
        elif test[1][-2:] == "in":
            if int(test[1][:-2]) < 59 or int(test[1][:-2]) > 76:
                this_pass_valid = False
        else:
            this_pass_valid = False
    elif test[0] == "hcl":
        # # followed by exactly six characters 0-9 or a-f
        match = re.search("^#([0-9a-f]){6}$", test[1])
        if not match:
            this_pass_valid = False
    elif test[0] == "ecl":
        if test[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            this_pass_valid = False
    elif test[0] == "pid":
        if len(test[1]) != 9 or isinstance(test[1], int) == False:
            this_pass_valid = False

    if this_pass_valid:
        print("FAIL" + str(test))
    else:
        print("PASS")