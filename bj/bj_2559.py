n, k = map(int, input().split())
temp = list(map(int, input().split()))

temp_sum = sum(temp[:k])
max_temp = temp_sum
for i in range(k, n):
    temp_sum = temp_sum + temp[i] - temp[i - k]
    max_temp = max(max_temp, temp_sum)

print(max_temp)
