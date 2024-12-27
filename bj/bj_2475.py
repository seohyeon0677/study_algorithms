num = list(map(int, input().split()))

sumnum = 0
for i in range(5):
    sumnum += num[i] ** 2

print(sumnum % 10)
