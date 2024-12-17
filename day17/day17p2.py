import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

regA = int(lines[0][12:])
regB = int(lines[1][12:])
regC = int(lines[2][12:])
instructions = list(map(int, lines[4][9:].split(',')))

#attempt at brute force from 8**16 to 8**17 (did not work)
"""
def tryA(rA, rB, rC):
    global target
    outputLen = 0
    n = len(instructions)
    ptr = 0
    while ptr < n:
        opcode = instructions[ptr]
        operand = instructions[ptr + 1]
        if opcode == 0:
            rA = rA // (2 ** getCombo(operand, rA, rB, rC))
            ptr += 2
        elif opcode == 1:
            rB = rB ^ operand
            ptr += 2
        elif opcode == 2:
            rB = getCombo(operand, rA, rB, rC) % 8
            ptr += 2
        elif opcode == 3:
            if rA != 0:
                ptr = operand
            else:
                ptr += 2
        elif opcode == 4:
            rB ^= rC
            ptr += 2
        elif opcode == 5:
            if outputLen >= n:
                return False
            res = getCombo(operand, rA, rB, rC) % 8
            if instructions[outputLen] != res:
                print('fail', outputLen)
                return False
            outputLen += 1
            ptr += 2
        elif opcode == 6:
            rB = rA // (2 ** getCombo(operand, rA, rB, rC))
            ptr += 2
        elif opcode == 7:
            rC = rA // (2 ** getCombo(operand, rA, rB, rC))
            ptr += 2
    return outputLen == n

def getCombo(val, regA, regB, regC):
    if val <= 3:
        return val
    if val == 4:
        return regA
    if val == 5:
        return regB
    if val == 6:
        return regC
"""

"""
Break down of the program:
regB = regA % 8
regB = regB ^ 1
regC = regA // (2 ** (regB))
regB = regB ^ 5
regB ^= regC
regA = regA // 8
print(regB % 8)
if A != 0 loop back to start
"""

cur = [0]
xor1, xor2 = 1, 5
#build from the end
for digit in reversed(instructions):
    newCur = []
    for a in cur:
        #left shift three bits (one octal place) and try new digit between 0 - 7
        mn = (a << 3) if a >= 1 else 1
        mx = (a << 3) + 8
        for possible in range(mn, mx):
            #simulate the operations above
            regB = possible % 8
            regC = possible // (2 ** (regB ^ xor1))
            #output digit = [(regB) ^ 1 ^ 5 ^ regC] % 8
            if (regB ^ xor1 ^ xor2 ^ regC) % 8 == digit:
                #left shift and add on to the end
                newCur.append((a << 3) + (regB))
    cur = newCur

#all should work
# for c in cur:
#     print(c, tryA(c, regB, regC))

ans = min(cur)
print(ans)