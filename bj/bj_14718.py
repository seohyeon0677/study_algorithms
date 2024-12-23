n, k = map(int, input().split())

enemy = [(i, *map(int, input().split())) for i in range(n)]

# 적을 각 스탯별로 오름차순 정렬한 다음 모든 스탯에서 동일한 k명이 포함되도록

power = sorted(enemy, key=lambda x: x[1])
speed = sorted(enemy, key=lambda x: x[2])
intelligence = sorted(enemy, key=lambda x: x[3])


#print(point)