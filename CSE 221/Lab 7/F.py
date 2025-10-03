import heapq

N,M,S,D=map(int,input().split())
g=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    g[u].append((v,w))
    g[v].append((u,w))

INF=10**18
first=[INF]*(N+1)
second=[INF]*(N+1)
first[S]=0
pq=[(0,S)]

while pq:
    d,u=heapq.heappop(pq)
    for v,w in g[u]:
        nd=d+w
        if nd<first[v]:
            second[v]=first[v]
            first[v]=nd
            heapq.heappush(pq,(nd,v))
        elif first[v]<nd<second[v]:
            second[v]=nd
            heapq.heappush(pq,(nd,v))

print(-1 if second[D]==INF else second[D])
