import heapq

N, M, S, T = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nxt, wt in graph[node]:
            if dist[nxt] > d + wt:
                dist[nxt] = d + wt
                heapq.heappush(pq, (dist[nxt], nxt))
    return dist

distA = dijkstra(S)
distB = dijkstra(T)

best_time = float('inf')
best_node = -1
for i in range(1, N + 1):
    if distA[i] != float('inf') and distB[i] != float('inf'):
        meet_time = max(distA[i], distB[i])
        if meet_time < best_time or (meet_time == best_time and i < best_node):
            best_time = meet_time
            best_node = i
if best_node == -1:
    print(-1)
else:
    print(best_time, best_node)
