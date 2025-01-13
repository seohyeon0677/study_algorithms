def choice(start, N, M, current):
    if len(current) == M:
        print(" ".join(map(str, current)))
        return
    
    for i in range(start, N + 1):
        current.append(i)
        choice(i + 1, N, M, current)
        current.pop()

N, M = map(int, input().split())

choice(1, N, M, [])
