def count_candy(tc, r, c):
    candy = 0
    for i in range(r):
        for j in range(c-2):
            if tc[i][j] == '>' and tc[i][j+1] == 'o' and tc[i][j+2] == '<':
                candy += 1
    for i in range(r-2):
        for j in range(c):
            if tc[i][j] == 'v' and tc[i+1][j] == 'o' and tc[i+2][j] == '^':
                candy += 1
    return candy


t = int(input().strip())    # test case 수

results = []
for _ in range(t):
    input()
    r, c = map(int, input().split())    # r:행  c:열
    tc = [input().strip() for _ in range(r)]
    results.append(count_candy(tc, r, c))

for result in results:
    print(result)
