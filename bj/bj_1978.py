N = int(input())
numbers = list(map(int, input().split()))

answer = 0
for i in range(N):
    if numbers[i] != 1:
        count = 0
        for j in range(1, numbers[i]):
            if numbers[i] % j == 0:
                count += 1
        if count == 1:
            answer += 1

print(answer)
