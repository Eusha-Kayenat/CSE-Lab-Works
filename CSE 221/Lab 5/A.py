from collections import deque

N, M = map(int, input().split())
adj = [[] for i in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N + 1)
order = []
q = deque([1])
visited[1] = True

while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)

print(*order)
