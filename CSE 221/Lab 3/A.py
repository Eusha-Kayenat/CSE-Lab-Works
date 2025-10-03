def merge(left, right):
    merged = []
    i = j = count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i 
            j += 1

    merged += left[i:]
    merged += right[j:]
    return merged,count

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr)//2
        left_sorted, left_inv = mergeSort(arr[:mid])
        right_sorted, right_inv = mergeSort(arr[mid:])
        merged, merge_inv = merge(left_sorted, right_sorted)
        total_inv = left_inv + right_inv + merge_inv
        return merged, total_inv

n = int(input())
arr = list(map(int, input().split()))
sorted_arr, inv_count = mergeSort(arr)
print(inv_count)
print(' '.join(map(str, sorted_arr)))
