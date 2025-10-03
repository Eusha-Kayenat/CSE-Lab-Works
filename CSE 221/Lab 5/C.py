from collections import deque

n, m, S, D = map(int, input().split())
adj = [[] for _ in range(n+1)]

if m:
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    for i in range(m):
        adj[u[i]].append(v[i])
        adj[v[i]].append(u[i])
for x in adj: x.sort()

dist, par = [-1]*(n+1), [-1]*(n+1)
q = deque([S]); dist[S] = 0

while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v], par[v] = dist[u]+1, u
            q.append(v)

if dist[D] == -1: print(-1)
else:
    path = []
    while D != -1: path.append(D); D = par[D]
    print(dist[path[0]])
    print(*path[::-1])
