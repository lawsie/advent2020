with open("input.txt") as f:
    data = f.readlines()

# Get rid of the newlines
data = [n.strip() for n in data]

FIELD_WIDTH = len(data[0]) -1 # Zero index
FIELD_HEIGHT = len(data) - 1

char_x = 0
char_y = 0
trees_found = 0
tracked_list = [list(data[0])]

# Run until you reach the bottom
while char_y < FIELD_HEIGHT:

    # Cater for the fact that the field repeats
    if char_x + 3 > FIELD_WIDTH:
        char_x = (char_x + 3) - FIELD_WIDTH - 1
    else:
        char_x += 3

    char_y += 1
        
    print("x is " + str(char_x) + " and y is " + str(char_y))
    print("Found " + str(trees_found) + " trees so far")

    if data[char_y][char_x] == "#":
        trees_found += 1

    # Record that you went here for debugging
    this_row = list(data[char_y])
    this_row[char_x] = "@"
    tracked_list.append(this_row)


[print(n) for n in tracked_list]
print(trees_found)