n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for i in range(m):
    adj[u[i]].append(v[i])
    adj[v[i]].append(u[i])

vis = [0]*(n+1)
ans = []
stack = [1]

while stack:
    x = stack.pop()
    if vis[x]: continue
    vis[x] = 1
    ans.append(x)
    for y in adj[x]:
        if not vis[y]:
            stack.append(y)

print(*ans)
