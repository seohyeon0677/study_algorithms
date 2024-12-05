numbers = list(map(int, input().split()))
numbers.sort()

max_num = numbers[2] * numbers[3] * numbers[4]

for answer in range(numbers[2], max_num + 1):
    count = 0
    for i in range(0, 5):
        if answer % numbers[i] == 0:
            count += 1
    if count >= 3:
        print(answer)
        break
