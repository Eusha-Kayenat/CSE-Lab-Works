def find_kth(k, x):
    low = 1
    high= k*x

    while low < high:
        mid = (low + high) // 2
        if mid - mid // x < k:
            low = mid + 1
        else:
            high = mid
    return low
T = int(input())
for _ in range(T):
    k, x = map(int, input().split())
    print(find_kth(k, x))
