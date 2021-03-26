# #DAY 2

# #add_to_pc?

# LDI = 0b10000010
# HLT = 0b00000001
# pc = 0
# mem = [
#     LDI,
#     3,
#     3,
#     HLT
# ] 
# #operand_size = LDI >> 6
# #add_to_pc = operand_size + 1

# # DECODE
# inst = mem[pc]
# add_to_pc = (inst >> 6) + 1 

# # print(operand_size)

# pc += add_to_pc

# print(mem[pc])

import sys

if len(sys.argv) !=2:
    #print the usage
    print(f"USAGE: {sys.argv[0]} <filename> ")
    #exit
    sys.exit(1)

file_name = sys.argv[1]
# print(file_name)
try:
    with open(file_name) as f:
        for line in f:
            print(line)
except FileNotFoundError: 
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)