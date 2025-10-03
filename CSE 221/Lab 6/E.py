import heapq

N = int(input())
words = [input().strip() for _ in range(N)]

graph = {}
in_degree = {}

for word in words:
    for c in word:
        if c not in graph:
            graph[c] = set()
            in_degree[c] = 0

for i in range(N-1):
    w1, w2 = words[i], words[i+1]
    for j in range(min(len(w1), len(w2))):
        if w1[j] != w2[j]:
            if w2[j] not in graph[w1[j]]:
                graph[w1[j]].add(w2[j])
                in_degree[w2[j]] += 1
            break
    else:
        if len(w1) > len(w2):
            print(-1)
            exit()

heap = [c for c in in_degree if in_degree[c] == 0]
heapq.heapify(heap)
order = []

while heap:
    c = heapq.heappop(heap)
    order.append(c)
    for nei in graph[c]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            heapq.heappush(heap, nei)

if len(order) == len(graph):
    print(''.join(order))
else:
    print(-1)
