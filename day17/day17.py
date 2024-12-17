import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

regA = int(lines[0][12:])
regB = int(lines[1][12:])
regC = int(lines[2][12:])
instructions = list(map(int, lines[4][9:].split(',')))
n = len(instructions)
ptr = 0

def getCombo(val):
    if val <= 3:
        return val
    if val == 4:
        return regA
    if val == 5:
        return regB
    if val == 6:
        return regC
    
output = ''

while ptr < n:
    opcode = instructions[ptr]
    operand = instructions[ptr + 1]
    if opcode == 0:
        regA = regA // (2 ** getCombo(operand))
        ptr += 2
    elif opcode == 1:
        regB = regB ^ operand
        ptr += 2
    elif opcode == 2:
        regB = getCombo(operand) % 8
        ptr += 2
    elif opcode == 3:
        if regA != 0:
            ptr = operand
        else:
            ptr += 2
    elif opcode == 4:
        regB ^= regC
        ptr += 2
    elif opcode == 5:
        output += f'{getCombo(operand) % 8},'
        ptr += 2
    elif opcode == 6:
        regB = regA // (2 ** getCombo(operand))
        ptr += 2
    elif opcode == 7:
        regC = regA // (2 ** getCombo(operand))
        ptr += 2
    
print(output[:-1])