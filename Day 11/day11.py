with open("input.txt") as f:
    data = f.readlines()

# Convert to 2d array otherwise the strings won't be mutable
data = [[char for char in n.strip()] for n in data]

#print("DATA -----------------")
#[print(n) for n in data]

# x, y coords for all check positions
def positions_to_check(x, y, data):
    last_col = len(data[0])-1
    last_row = len(data)-1

    positions = [ [x-1, y-1], [x, y-1], [x+1, y-1],
                        [x-1, y], [x+1, y],
                        [x-1, y+1], [x, y+1], [x+1, y+1]
    ]
    surroundings = []
    for position in positions:
        if position[0] >= 0 and position[0] <= last_row and position[1] >= 0 and position[1] <= last_col:
            surroundings.append(data[position[0]][position[1]])
    return surroundings

def iterate(data):
    cols = len(data[0])
    rows = len(data)

    # Fill up new array with dummy values
    new_config = []
    any_changes = False
    
    # Loop through
    for row in range(rows):
        new_row = ["X" for i in range(cols)]
        for col in range(cols):
            # Get the positions to check
            surroundings = positions_to_check(row, col, data)
            #print(row, col, surroundings)
            
            # Make the changes to the new config
            if data[row][col] == "L" and "#" not in surroundings:
                new_row[col] = "#"
                any_changes = True
            elif data[row][col] == "#" and surroundings.count("#") >= 4:
                new_row[col] = "L"
                any_changes = True
            else:
                new_row[col] = data[row][col]
        new_config.append(new_row)

    if not any_changes:
        print("No changes")
        occupied_seats = 0
        for i in new_config:
            occupied_seats += i.count("#")
        print(occupied_seats)
        return False
    else:
        return new_config
    
# Make a copy of newdata to initialise
newdata = data.copy()

#print("COPY OF DATA -----------------")
#[print(n) for n in newdata]

while newdata is not False:
    newdata = iterate(newdata)
   # print("ITERATION -----------------")
    #[print(n) for n in newdata]