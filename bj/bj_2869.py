A, B, V = map(int, input().split())

H = 0
days = 0
while True:
    days += 1
    H += A
    if H >= V:
        break
    H -= B

print(days)
