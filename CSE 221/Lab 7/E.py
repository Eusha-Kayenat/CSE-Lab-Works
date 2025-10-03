import heapq

N,M=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))

g=[[] for _ in range(N+1)]
for i in range(M):
    g[u[i]].append((v[i],w[i]))

INF=10**18
dist=[[INF,INF] for _ in range(N+1)]
pq=[(0,1,-1)] 

while pq:
    c,n,p0=heapq.heappop(pq)
    for nei,wt in g[n]:
        p=wt%2
        if p0!=p and c+wt<dist[nei][p]:
            dist[nei][p]=c+wt
            heapq.heappush(pq,(dist[nei][p],nei,p))

res=min(dist[N])
print(-1 if res==INF else res)
