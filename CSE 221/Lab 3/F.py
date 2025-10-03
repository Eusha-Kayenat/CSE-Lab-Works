def get_balanced_order(arr):
    result = []

    def build_order(left, right):
        if left > right:
            return
        mid = (left + right) // 2
        result.append(arr[mid])       
        build_order(left, mid - 1)      
        build_order(mid + 1, right)

    build_order(0, len(arr) - 1)
    return result
n = int(input())
arr = list(map(int, input().split()))

order = get_balanced_order(arr)
print(' '.join(map(str, order)))
