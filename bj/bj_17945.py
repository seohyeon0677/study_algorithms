a, b = map(int, input().split())

x1 = int(-a + (a**2 - b)**0.5)
x2 = int(-a - (a**2 - b)**0.5)

if x1 == x2:
    print(x1)
else:
    print(x2, x1)
