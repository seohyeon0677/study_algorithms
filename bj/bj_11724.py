def dfs(graph, node, visited):
    stack = [node]
    while stack:
        current = stack.pop(0)
        if not visited[current]:
            visited[current] = True
            stack.extend(graph[current])

def count_connect(n, graph):
    visited = [False] * (n + 1)
    components = 0

    for node in range(1, n + 1):
        if not visited[node]:
            dfs(graph, node, visited)
            components += 1
    
    return components


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(count_connect(N, graph))
