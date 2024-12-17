n = int(input())

location = [tuple(map(int, input().split())) for _ in range(n)]

# 색종이 영역 set 만들기
paper = set()

for i in range(n):
    for j in range(0, 10):
        for k in range(0, 10):
            x = location[i][0] + j
            y = location[i][1] + k
            paper.add((x,y))

print(len(paper))
