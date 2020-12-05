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
    print("PASSPORT[" + str(num) + "] - " + str(passport))

    # Remove all present fields from the list
    for field in passport:
        if field[:3] in check_fields:
            check_fields.remove(field[:3])
    
    # If there are any remaining, check if it's cid. If so, or there are none, then it's ok
    if len(check_fields) == 1 and check_fields[0] == "cid" or len(check_fields) == 0:
        number_valid += 1
        
    else:
        print("INVALID: " + str(check_fields))


print("There are " + str(number_valid) + " valid passports out of " + str(len(data)))


