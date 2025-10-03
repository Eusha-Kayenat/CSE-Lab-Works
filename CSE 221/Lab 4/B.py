N, M = map(int, input().split())

if M > 0:
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
else:
    u = v = w = []

list = [[] for i in range(N + 1)] 

for i in range(M):
    list[u[i]].append((v[i], w[i]))

for i in range(1, N + 1):
    print(f"{i}:", end='')
    for neighbor, weight in list[i]:
        print(f" ({neighbor},{weight})", end='')
    print()
