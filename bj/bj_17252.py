from itertools import combinations

def samsam(N):
    num_list = []
    num = 1
    while num <= N:
        num_list.append(num)
        num *= 3

    for r in range(1, len(num_list) + 1):
        for subset in combinations(num_list, r):
            if sum(subset) == N:
                return "YES"
    return "NO"

N = int(input())
print(samsam(N))
