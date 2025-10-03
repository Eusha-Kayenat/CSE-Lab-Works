import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
M = int(data[1])
degree = [0]*(N + 1)

u = list(map(int, data[2:2+M]))
v = list(map(int, data[2+M:2+2*M]))

for i in range(M):
    degree[u[i]] += 1
    degree[v[i]] += 1

odd = 0
for i in degree[1:]:
    if i % 2 == 1:
        odd += 1
if odd == 0 or odd == 2:
    print("YES")
else:
    print("NO")
