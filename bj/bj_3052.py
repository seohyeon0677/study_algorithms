nums = [int(input()) for _ in range(10)]

nums42 = [num % 42 for num in nums]

nums42_set = set(nums42)

print(len(nums42_set))
