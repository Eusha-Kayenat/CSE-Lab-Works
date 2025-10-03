N, M, K = map(int, input().split())
 
knights = set()
for _ in range(K):
    x, y = map(int, input().split())
    knights.add((x, y))
 
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]
 
for x, y in knights:
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if (nx, ny) in knights:
            print("YES")
            exit()
 
print("NO")
