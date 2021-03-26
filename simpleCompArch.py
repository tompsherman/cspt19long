import sys

"""
computer architecture:

numbering systems

data-driven machine:

what components are of a computer and what they mean to us?
---- data-driven machine that does stuff

what is a CPU to us
---- unit that asks what next?
---- FETCH, DECODE, EXECUTE cycle

what are registers to us
---- tiny, superfast pieces of memory built into the CPU

what is RAM / memory to us
---- the store that holds the instructions and data that the CPU is asking for
---- a place for a software engineer to store a program (instructions and data)

to build a computer:
need memory (a list or array) --- contiguous block of memory
instructions to tell CPU to do something for decode cycle
and the decode cycle to take something from memory 
-- program counter to keep track of where we are in the memory at a given time
-- state whether the system is running or not

upcodes,
if its in program how would you add it
fetch decode execute

DAY 2

add_to_pc?

LDI = 0b10000010

operand_size = LDI >> 6

print(operand_size)
"""

#some instructions for the cpu
PRINT_TOM = 0b01011010 # print "tom" to console
PRINT_NUM = 0b10010000 # print a number stored in ram 1 byte ahead of instruction
HALT    =   0b10110111 # halt the operation of our data driven machine
STORE    =  0b00010001 # store a number from the ram 2 bytes ahead of instruction into a register denoted from 1 byte ahead of the instructionin ram (LDI)
PRINT_REG = 0b01111101 # print a number at the index into registers provided by the number from current instruction +1 in ram 
ADD     =   0b01101101 # adds the num stored at the register at the index from ram 1 byte away from the instruction


ram = [0] * 256

def load_mem(filename):
    try:
        address = 0
        with open(filename) as f:
            for line in f:
                # split the line on #
                comment_split = line.split('#')
                # strip the data
                data = comment_split[0].strip()
                # deal with empty blank lines
                if data == '':
                    continue
                # extract the value (convert to int)
                val = int(data, 2)
                # store the val in ram at current address?
                ram[address] = val
                # increment address
                address += 1
    except FileNotFoundError:
        print(f"{sys.argv[0]}: {sys.argv[1]} not found")
        sys.exit(2)

# #list for RAM
# ram = [
#     PRINT_TOM,
#     PRINT_NUM,
#     23,
#     STORE,
#     1,
#     10,
#     STORE,
#     3,
#     20,
#     PRINT_REG,
#     1,
#     PRINT_REG,
#     3,
#     ADD,
#     1,
#     3,
#     PRINT_REG,
#     1,
#     PRINT_REG,
#     3,
#     HALT
# ]
if len(sys.argv) != 2:
    print("some usage message here...")
    sys.exit(1)
    
load_mem(sys.argv[1])
# program counter (instruction pointer) to keep track of what we are executing
pc = 0

# registers
registers = [0] * 8 # reg0 - reg7

#loop for CPU execute cycle
while True:
    # FETCH
    instruction = ram[pc]

    # DECODE
    if instruction == HALT:
        # EXECUTE
        break
    # DECODE
    elif instruction == PRINT_TOM:
        # EXECUTE
        print("Tom") 
        pc += 1    
    # DECODE
    elif instruction == PRINT_NUM:
        # EXECUTE
        num = ram[pc+1]
        print(num)
        pc += 2   
    # DECODE
    elif instruction == STORE:
        # EXECUTE
        reg_index = ram[pc+1]
        num = ram[pc+2]
        registers[reg_index] = num
        pc += 3  
    # DECODE
    elif instruction == PRINT_REG:
        # EXECUTE
        reg_index = ram[pc+1]
        num = registers[reg_index]
        print(num)
        pc += 2   
    # DECODE
    elif instruction == ADD:
        # EXECUTE
        reg_index_A = ram[pc+1]
        reg_index_B = ram[pc+2]

        registers[reg_index_A] = registers[reg_index_A] + registers[reg_index_B]
        pc += 3  
    # DECODE
    else:
        # EXECUTE
        print("ERROR! ERROR!")
        break

