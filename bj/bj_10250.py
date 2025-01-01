T = int(input())
tc = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    H, W, N = tc[i][0], tc[i][1], tc[i][2]  # H(층), W(방), N(손님)
    n = N // H + 1
    f = N % H

    if n < 10:
        print(f"{f}0{n}")
    else:
        print(f"{f}{n}")
    