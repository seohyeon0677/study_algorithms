def find(N, K):
    visited = [False] * 100001

    stack = [(N, 0)]
    visited[N] = True

    while stack:
        current, time = stack.pop(0)

        if current == K:
            return time
        
        for next in (current - 1, current + 1, current * 2):
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = True
                stack.append((next, time + 1))

N, K = map(int, input().split())

print(find(N, K))
