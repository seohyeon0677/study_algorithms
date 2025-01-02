T = int(input())
TC = [list(input().split()) for _ in range(T)]

for i in range(T):
    R, S = int(TC[i][0]), TC[i][1]
    answer = ''.join(s * R for s in S)
    print(answer)
