import heapq

N,M,S,D=map(int,input().split())
w=[0]+list(map(int,input().split()))
g=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    g[u].append(v)

INF=10**18
dist=[INF]*(N+1)
dist[S]=w[S]
pq=[(w[S],S)]

while pq:
    c,u=heapq.heappop(pq)
    if c>dist[u]: continue
    for v in g[u]:
        nc=c+w[v]
        if nc<dist[v]:
            dist[v]=nc
            heapq.heappush(pq,(nc,v))

print(-1 if dist[D]==INF else dist[D])
