T = int(input())
answers = [input() for _ in range(T)]

for answer in answers:
    count = 0
    point = 0
    for i in answer:
        if i == 'O':
            count += 1
            point += count
        else:
            count = 0

    print(point)
