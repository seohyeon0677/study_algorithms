n = int(input())
s_list = [int(input()) for _ in range(n)]

for s in range(n):
    key = []
    number = s_list[s]
    for i in range(2, 1000001):
        if number % i == 0:
            key.append(i)
    if len(key) == 0:
        print("YES")
    else:
        print("NO")
