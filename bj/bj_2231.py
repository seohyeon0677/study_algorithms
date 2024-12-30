N = int(input())

for n in range(1, N):
    n_str = str(n)
    n_list = [int(n_str[i]) for i in range(len(n_str))]
    n_sum = sum(n_list)

    if n + n_sum == N:
        break

print(n)
