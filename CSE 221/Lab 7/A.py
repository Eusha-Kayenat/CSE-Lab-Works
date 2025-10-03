import heapq

N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for i in range(M):
    graph[u[i]].append((v[i], w[i]))

dist = [float('inf')] * (N + 1)
parent = [-1] * (N + 1)
dist[S] = 0

pq = [(0, S)] 
while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue
    for nxt, wt in graph[node]:
        if dist[nxt] > d + wt:
            dist[nxt] = d + wt
            parent[nxt] = node
            heapq.heappush(pq, (dist[nxt], nxt))

if dist[D] == float('inf'):
    print(-1)
else:
    path = []
    cur = D
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print(dist[D])
    print(*path)
