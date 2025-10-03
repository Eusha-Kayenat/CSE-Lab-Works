from bisect import bisect_right

def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, invrs_l = merge_sort_and_count(arr[:mid])
    right, invrs_r = merge_sort_and_count(arr[mid:])
    merged, invrs_split = merge_and_count_special(left, right)

    return merged, invrs_l + invrs_r + invrs_split

def merge_and_count_special(left, right):
    merged = []
    invrs_c = 0

    right_squares = sorted([x * x for x in right])

    for val in left:
        c = bisect_right(right_squares, val - 1)
        invrs_c += c


    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, invrs_c
n = int(input())
A = list(map(int, input().split()))

_, c = merge_sort_and_count(A)
print(c)
