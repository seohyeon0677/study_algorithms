up, down, V = map(int, input().split())

v = V - up
d = v // (up - down) if v % (up - down) == 0 else v // (up - down) + 1

print(d + 1)
