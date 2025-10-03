import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    x, y = map(int, input().split())
    l = bisect.bisect_left(a, x)
    r = bisect.bisect_right(a, y)
    print(r - l)
