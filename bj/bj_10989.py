import sys

N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()

# 한 번에 출력
sys.stdout.write("\n".join(map(str, nums)) + "\n")
