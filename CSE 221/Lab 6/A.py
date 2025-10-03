from collections import deque

N, M = map(int, input().split())
g = [[] for i in range(N+1)]
in_degree = [0]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)

order = []
while q:
    u = q.popleft()
    order.append(u)
    for v in g[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            q.append(v)

if len(order) == N:
    print(*order)
else:
    print(-1)
