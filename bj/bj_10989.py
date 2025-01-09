import sys
def input():
    return sys.stdin.readline()

N = int(input())
nums = [0] * 10001
for _ in range(N):
    n = int(input())
    nums[n] += 1

for i in range(1, 10001):
    for _ in range(nums[i]):
        print(i)
