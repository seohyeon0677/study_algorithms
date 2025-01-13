from collections import deque

def virus(n, edges):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n+1)

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        count = 0
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        return count
    
    return bfs(1)

n = int(input())
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(virus(n, edges))
