import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

INF = 10**18
danger = [INF]*(N+1)
danger[1] = 0

pq = [(0,1)]
while pq:
    d, u = heapq.heappop(pq)
    if d > danger[u]: 
        continue
    for v, w in g[u]:
        new_d = max(d, w)
        if new_d < danger[v]:
            danger[v] = new_d
            heapq.heappush(pq, (new_d, v))

for i in range(1, N+1):
    if danger[i] == INF:
        print(-1, end=" ")
    else:
        print(danger[i], end=" ")
