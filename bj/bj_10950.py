T = int(input())
numbers = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    print(numbers[i][0] + numbers[i][1])
