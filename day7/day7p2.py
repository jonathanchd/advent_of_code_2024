import sys
import math
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

ans = 0

def search(index, curr, target, nums):
    if curr > target:
        return False
    if index == len(nums) - 1:
        if curr == target:
            return True
        return False
    res1 = search(index + 1, curr * nums[index + 1], target, nums)
    if res1:
        return True
    res2 = search(index + 1, curr + nums[index + 1], target, nums)
    if res2:
        return True
    return search(index + 1, int(str(curr) + str(nums[index + 1])), target, nums)
        

for line in lines:
    line = line.split(":")
    target = int(line[0])
    nums = list(map(int, line[1].strip().split(" ")))
    if search(0, nums[0], target, nums):
        ans += target

print(ans)