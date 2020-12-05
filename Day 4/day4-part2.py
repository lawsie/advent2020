import re

data = []
number_valid = 0
valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

# Open the file and read in the records (take a newline as a break in records)
with open("input.txt") as f:
    current_record = []

    for line in f:

        if line != "\n":
            current_record = current_record + line.split(" ")

        else:
            current_record = [n.strip() for n in current_record]
            data.append(current_record)
            current_record = []
    
    # Don't forget the last one!! Doh
    data.append(current_record)

for num, passport in enumerate(data):

    check_fields = valid_fields.copy()
    #print("PASSPORT[" + str(num) + "] - " + str(passport))

    # Remove all present fields from the list
    for field in passport:
        if field[:3] in check_fields:
            check_fields.remove(field[:3])
    
    # If there are any remaining, check if it's cid. If so, or there are none, then it's ok
    if (len(check_fields) == 1 and check_fields[0] == "cid") or len(check_fields) == 0:
        
        # Now validate each field!
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

        # Passport is a list of fields in xxx:val format fyi

        # Assert it's true unless it fails any validation checks
        this_pass_valid = []

        for field in passport:
            # Get the type of field and the data as a list
            fvalues = field.split(":")
            
            
            if fvalues[0] == "byr":
                if int(fvalues[1]) < 1920 or int(fvalues[1]) > 2002:
                    print("byr " + str(fvalues[1]) + " not between 1920 and 2002")
                    this_pass_valid.append(False)
            elif fvalues[0] == "iyr":
                if int(fvalues[1]) < 2010 or int(fvalues[1]) > 2020:
                    print("iyr " + str(fvalues[1]) + " not between 2010 and 2020")
                    this_pass_valid.append(False)
            elif fvalues[0] == "eyr":
                if int(fvalues[1]) < 2020 or int(fvalues[1]) > 2030:
                    print("eyr " + str(fvalues[1]) + " not between 2020 and 2030")
                    this_pass_valid.append(False)
            elif fvalues[0] == "hgt":
                if fvalues[1][-2:] == "cm":
                    if int(fvalues[1][:-2]) < 150 or int(fvalues[1][:-2]) > 193:
                        print("hgt in cm " + str(fvalues[1]) + " not between 150 and 193")
                        this_pass_valid.append(False)
                elif fvalues[1][-2:] == "in":
                    if int(fvalues[1][:-2]) < 59 or int(fvalues[1][:-2]) > 76:
                        print("hgt in in " + str(fvalues[1]) + " not between 59 and 76")
                        this_pass_valid.append(False)
                else:
                    print("hgt " + str(fvalues[1]) + " not either cm or inches")
                    this_pass_valid.append(False)
            elif fvalues[0] == "hcl":
                # # followed by exactly six characters 0-9 or a-f
                match = re.search("^#([0-9a-f]){6}$", fvalues[1])
                if not match:
                    print("hcl " + str(fvalues[1]) + " not # then 0-9/a-z *6")
                    this_pass_valid.append(False)
            elif fvalues[0] == "ecl":
                if fvalues[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    print("ecl " + str(fvalues[1]) + " not amb, blu, brn, gry, grn, hzl, oth")
                    this_pass_valid.append(False)
            elif fvalues[0] == "pid":
                if len(fvalues[1]) != 9:
                    print("pid " + str(fvalues[1]) + " not length 9")
                    this_pass_valid.append(False)  
                if fvalues[1].isdigit() == False:
                    print("pid " + str(fvalues[1]) + " not integer")
                    this_pass_valid.append(False)

        if len(this_pass_valid) == 0:
            number_valid += 1
        else:
            print("INVALID" + str(passport))

        print("------------")



print("There are " + str(number_valid) + " valid passports out of " + str(len(data)))

# 176 too high
# 162 is too low