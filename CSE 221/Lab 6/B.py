from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

color = [-1]*(N+1)

def bfs(start):
    q = deque([start])
    color[start] = 0
    count = [1, 0]
    
    while q:
        u = q.popleft()
        for v in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                count[color[v]] += 1
                q.append(v)
            elif color[v] == color[u]:
                pass
    return max(count)

ans = 0
for i in range(1, N+1):
    if color[i] == -1:
        ans += bfs(i)

print(ans)
