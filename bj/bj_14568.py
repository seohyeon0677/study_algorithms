# 남규a >= 영훈b + 2
# 택희c 홀수개 안됨
# 남는 사탕 없음
# 모두 하나 이상 받아야 함

candy = int(input())

count = 0
for a in range(1, candy-1):
    for b in range(1, candy-a-1):
        c = candy - a - b
        if a >= b + 2:
            if c % 2 != 1:
                count += 1
print(count)
