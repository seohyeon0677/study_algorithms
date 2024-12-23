n, k = map(int, input().split())
temp = list(map(int, input().split()))

temp_sums = []
for i in range(0, n-k+1):
    temp_sum = sum(temp[i:i+k])
    temp_sums.append(temp_sum)

print(max(temp_sums))
