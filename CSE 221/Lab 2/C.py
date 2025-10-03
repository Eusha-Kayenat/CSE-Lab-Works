n, x = map(int, input().split())
a = list(map(int, input().split()))

elements = [(a[i], i + 1) for i in range(n)]
elements.sort()

for i in range(n - 2):
    left = i + 1
    right = n - 1
    while left < right:
        current_sum = elements[i][0] + elements[left][0] + elements[right][0]
        if current_sum == x:
            print(elements[i][1], elements[left][1], elements[right][1])
            exit()
        elif current_sum < x:
            left += 1
        else:
            right -= 1
print(-1)
