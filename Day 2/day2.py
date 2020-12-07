with open("input.txt") as f:
    data = f.readlines()
valid_passwords = 0
for item in data:
    current = item.strip().split(" ")

    # How many times does the character appear in the list?
    letter = current[1][0]
    count = current[2].count(letter)
    #print(letter + " appears " + str(count) + " times in " + current[2])

    # Calculate the lower and upper bounds
    bounds = current[0].split("-")
    lower = int(bounds[0])
    upper = int(bounds[1])
    #print(str(lower) + " " + str(upper))

    if count >= lower and count <= upper:
        valid_passwords += 1

print("There were " + str(valid_passwords) + " valid passwords")
