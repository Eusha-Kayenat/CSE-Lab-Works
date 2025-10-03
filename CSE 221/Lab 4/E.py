import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
M = int(data[1])

u = list(map(int, data[2:2 + M]))
v = list(map(int, data[2 + M:2 + 2 * M]))
in_deg = [0] * (N + 1)
out_deg = [0] * (N + 1)

for i in range(M):
    out_deg[u[i]] += 1
    in_deg[v[i]] += 1

result = []
for i in range(1, N + 1):
    result.append(str(in_deg[i] - out_deg[i]))
print(' '.join(result))
