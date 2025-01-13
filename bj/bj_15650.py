def choice(N, M, current):
    if len(current) == M:
        print(" ".join(map(str, current)))
        return
    
    for i in range(1, N + 1):
        if not current or i > current[-1]:
            current.append(i)
            choice(N, M, current)
            current.pop()

N, M = map(int, input().split())

choice(N, M, [])
