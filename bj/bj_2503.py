
TC = int(input())

test = [list(map(int, input().split())) for _ in range(TC)]


answer = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):

            if (a==b or b==c or c==a):
                continue

            count = 0
            for i in range(len(test)):
                num = test[i][0]
                strike = test[i][1]
                ball = test[i][2]

                num1 = num // 100
                num2 = num % 100 // 10
                num3 = num % 10

                s_count = 0
                b_count = 0

                if a==num1: s_count +=1
                if b==num2: s_count +=1
                if c==num3: s_count +=1

                if b==num1: b_count +=1
                if c==num2: b_count +=1
                if a==num3: b_count +=1
                if c==num1: b_count +=1
                if a==num2: b_count +=1
                if b==num3: b_count +=1

                if s_count == strike and b_count == ball:
                    count += 1

            if count == TC:
                answer += 1

print(answer)

# def calcul(target, answer):
#     st = 0
#     b = 0
#     for i in range(len(target)):
#         if target[i] == answer[i]:
#             st += 1
#         if target[i] in list(answer) and target[i] != answer[i]:
#             b += 1
#     return st, b