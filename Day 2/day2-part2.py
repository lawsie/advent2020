with open("input.txt") as f:
    data = f.readlines()
    valid_passwords = 0
    for item in data:
        current = item.strip().split(" ")

        # Find the positions to check for that character
        positions = current[0].split("-")

        # Take off one because Python is zero indexed
        pos1 = int(positions[0]) - 1
        pos2 = int(positions[1]) - 1

        # Don't forget to use xor not or! (oops!)
        if (current[2][pos1] == current[1][0]) ^ (current[2][pos2] == current[1][0]):
            valid_passwords += 1
    
    print("There were " + str(valid_passwords) + " valid passwords")
