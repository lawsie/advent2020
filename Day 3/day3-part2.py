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
total_trees = []

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]


for slope in slopes:
    char_x = 0
    char_y = 0

    # Run until you reach the bottom
    while char_y < FIELD_HEIGHT:

        # Cater for the fact that the field repeats
        if char_x + slope[0] > FIELD_WIDTH:
            char_x = (char_x + slope[0]) - FIELD_WIDTH - 1
        else:
            char_x += slope[0]

        char_y += slope[1]
            
        print("x is " + str(char_x) + " and y is " + str(char_y))
        print("Found " + str(trees_found) + " trees so far")

        if data[char_y][char_x] == "#":
            trees_found += 1

        # Record that you went here for debugging
        #tracked_list.append(list(data[char_y-1])) # Debug for the vertical 2 jump
        this_row = list(data[char_y])
        this_row[char_x] = "@"
        tracked_list.append(this_row)

    total_trees.append(trees_found)
    trees_found = 0
    
    [print(n) for n in tracked_list]
    print(total_trees)

    total = 1
    for num in total_trees:
        total *= num
    print(total)