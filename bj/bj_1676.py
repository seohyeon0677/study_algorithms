N = int(input())

zero = 0
n = 5
while N >= n:
    zero += N // n
    n *= 5

print(zero)
