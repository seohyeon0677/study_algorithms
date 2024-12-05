mushroom = [int(input()) for _ in range(10)]

point = 0
point_max = 0
for i in range(len(mushroom)):
    point += mushroom[i]
    if (abs(100 - point) <= abs(100 - point_max)):
        point_max = point

print(point_max)
