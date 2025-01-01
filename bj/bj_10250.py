T = int(input())
tc = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    H, W, N = tc[i][0], tc[i][1], tc[i][2]  # H(층), W(방), N(손님)
    n = (N - 1) // H + 1
    f = H if N % H == 0 else N % H

    if n < 10:
        room = int(str(f) + '0' + str(n))
    else:
        room = int(str(f) + str(n))
    
    print(room)
