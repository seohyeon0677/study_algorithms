N = int(input())

count = 0
min_num = 1
max_num = 1
for i in range(N):
    if N >= min_num and N <= max_num:
        break
    count += 1
    min_num = max_num + 1
    max_num = max_num + count * 6

print(i + 1)
