a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)
count = 0
for i in range(10):
    i = str(i)
    for n in range(len(num)):
        if i == num[n]:
            count += 1
    print(count)
    count = 0
