import sys
input = sys.stdin.readline

def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if sz[a] < sz[b]: a, b = b, a
        p[b] = a
        sz[a] += sz[b]
    return sz[a]

n, k = map(int, input().split())
p = list(range(n+1))
sz = [1]*(n+1)

for _ in range(k):
    a, b = map(int, input().split())
    print(union(a, b))
