n = int(input())

columns = [tuple(map(int, input().split())) for _ in range(n)]

# 기둥 위치 기준으로 오름차순 정렬
# max h column 찾기
# max h 이전
    # 이전 기둥보다 높으면 height 올리기
# max h 이후
    # 반대로 진행

columns.sort(key=lambda x: x[0])

max_column = max(columns, key=lambda x: x[1])
max_column_index = columns.index(max_column)

area = 0

height = 0
for i in range(0, max_column_index + 1):
    if columns[i][1] > height:
        height = columns[i][1]
    if i < max_column_index:
        area += (columns[i+1][0] - columns[i][0]) * height

height = 0
for i in range(n-1, max_column_index, -1):
    if columns[i][1] > height:
        height = columns[i][1]
    area += height * (columns[i][0] - columns[i-1][0])

area += max_column[1]

print(area)
