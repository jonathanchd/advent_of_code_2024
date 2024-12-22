import sys
from collections import defaultdict
infile = sys.argv[1]
D = open(infile).read().strip()

lines = list(map(int, D.split('\n')))

ans = 0

def process(a):
    a = (a ^ (a * 64)) % 16777216
    a = (a ^ (a // 32)) % 16777216
    a = (a ^ (a * 2048)) % 16777216
    return a

window = defaultdict(lambda: 0)
for line in lines:
    digits = [line % 10]
    for i in range(2000):
        line = process(line)
        digits.append(line % 10)
    ans += line
    changes = [digits[i] - digits[i - 1] for i in range(1, len(digits))]
    digits = digits[1:]
    seen = set()
    for i in range(3, len(changes)):
        sequence = (changes[i - 3], changes[i - 2], changes[i - 1], changes[i])
        if sequence in seen:
            continue
        seen.add(sequence)
        window[sequence] += digits[i]

print(max(window.values()))