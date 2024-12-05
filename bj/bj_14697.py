room1, room2, room3, n = map(int, input().split())

count = 0
for a in range(n//room1+1):
    for b in range(n//room2+1):
        for c in range(n//room3+1):
            if a*room1 + b*room2 + c*room3 == n:
                if count >= 1:
                    break
                count += 1

if count == 1:
    print(1)
else:
    print(0)
