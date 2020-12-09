import copy

def run_program(data):
    acc = 0
    cir = 0
    used_instructions = []

    while cir not in used_instructions:
        #print("Executing instruction " + str(cir))
        used_instructions.append(cir)

        # Get the instruction and the argument
        if cir >= len(data):
            print("Tried to terminate, acc was ", acc)
        else:
            instruction = data[cir][0]
            arg = int(data[cir][1])

            if instruction == "acc":
                # Add the arg to the accumulator and move on
                acc += arg
                cir += 1
            elif instruction == "jmp":
                cir += arg
                pass
            elif instruction == "nop":
                # Just go to the next instruction
                cir += 1
            else:
                print("What's going on here")
       

    return False
  


with open("input.txt") as f:
    data = f.readlines()

# Get rid of newlines and make each into a list
data = [n.strip().split(" ") for n in data]

# Run the program lots of times, changing one instruction at a time
for i in range(len(data)):
    
    # Make a copy of data
    newdata = copy.deepcopy(data)

    # Modify instruction i unless it's an acc
    if newdata[i][0] == "jmp":
        newdata[i][0] = "nop"
        if run_program(newdata):
            break
    elif newdata[i][0] == "nop":
        newdata[i][0] = "jmp"
        if run_program(newdata):
            break
  

