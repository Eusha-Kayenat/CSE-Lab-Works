N, M = map(int, input().split())
matrix = [[0] * N for i in range(N)]

for i in range(M):
    u, v, w = map(int, input().split())
    matrix[u - 1][v - 1] = w

for row in matrix:
    print(' '.join(map(str, row)))
