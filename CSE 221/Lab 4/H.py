import sys
import math
input = sys.stdin.read

data = input().split()
N = int(data[0])
M = int(data[1])

adj_nodes = [[] for i in range(N + 1)] 

for i in range(1, N + 1):
    for j in range(1, N + 1):
        n = math.gcd(i, j)
        if i != j and n == 1:
            adj_nodes[i].append(j)
    adj_nodes[i].sort()

i = 2
res = []
for j in range(M):
    x = int(data[i])
    K = int(data[i + 1])
    i += 2

    if K <= len(adj_nodes[x]):
        res.append(str(adj_nodes[x][K - 1]))
    else:
        res.append("-1")

print('\n'.join(res))
