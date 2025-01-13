N = input()

nums = [0] * 10
for n in N:
    nums[int(n)] += 1
nums[6] += nums[9]
nums[6] = nums[6] // 2 if nums[6] % 2 == 0 else nums[6] // 2 + 1
nums[9] = 0

print(max(nums))
