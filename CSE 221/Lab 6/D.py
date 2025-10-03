from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    visited = [-1]*(N+1)
    queue = deque([start])
    visited[start] = 0
    farthest_node = start
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if visited[nei] == -1:
                visited[nei] = visited[node] + 1
                queue.append(nei)
                if visited[nei] > visited[farthest_node]:
                    farthest_node = nei
    return farthest_node, visited[farthest_node]
A, _ = bfs(1)
B, dist = bfs(A)

print(dist)
print(A, B)
