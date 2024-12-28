N = int(input())
T_size = list(map(int, input().split()))
T, P = map(int, input().split())

T_min = 0
for i in range(6):
    if T_size[i] % T == 0:
        T_min += T_size[i] // T
    else:
        T_min += T_size[i] // T + 1

P_max = N // P
P_one = N % P

print(T_min)
print(P_max, P_one)
