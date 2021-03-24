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

"""

#some instructions for the cpu
PRINT_TOM = 0b01011010 # print "tom" to console
PRINT_NUM = 0b10010000 # print a number stored in ram 1 byte ahead of instruction
HALT    =   0b10110111 # halt the operation of our data driven machine
STORE    =  0b00010001 # store a number from the ram 2 bytes ahead of instruction into a register denoted from 1 byte ahead of the instructionin ram
PRINT_REG = 0b01111101 # print a number at the index into registers provided by the number from current instruction +1 in ram 

#list for RAM
ram = [
    PRINT_TOM,
    PRINT_NUM,
    23,
    STORE,
    1,
    123,
    HALT
]

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
    else:
        # EXECUTE
        print("ERROR! ERROR!")
        break

