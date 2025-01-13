def choice(n, m, current):
    if len(current) == m:
        print(" ".join(map(str, current)))
        return
    
    for i in range(1, n + 1):
        if i not in current:
            current.append(i)
            choice(n, m, current)
            current.pop()

n, m = map(int, input().split())

choice(n, m, [])
