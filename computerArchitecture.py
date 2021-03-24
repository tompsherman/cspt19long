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

"""

#some instructions for the cpu
PRINT_TOM = 0b01011010 # print "tom" to console
PRINT_NUM = 0b10010000 # print a number stored in ram 1 byte ahead of instruction
HALT    =   0b10110111 # halt the operation of our data driven machine
SAVE    =   0b00010001 # store a number from the ram 2 bytes ahead of instruction into a register denoted from 1 byte ahead of the instructionin ram

#list for RAM
ram = [
    PRINT_TOM,
    PRINT_NUM,
    23,
    HALT
]

# program counter (instruction pointer) to keep track of what we are executing
pc = 0

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
    else:
        # EXECUTE
        print("ERROR! ERROR!")
        break

