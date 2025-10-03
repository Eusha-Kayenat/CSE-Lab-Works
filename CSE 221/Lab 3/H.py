def pre_order(in_start, in_end):
    if in_start > in_end:
        return []

    root_val = post_order[pre_order.post_index]
    pre_order.post_index -= 1

    in_index = in_order_map[root_val]

    right = pre_order(in_index + 1, in_end)
    left = pre_order(in_start, in_index - 1)

    return [root_val] + left + right

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_order_map = {val: idx for idx, val in enumerate(in_order)}

pre_order.post_index = n - 1
pre_order = pre_order(0, n - 1)

print(*pre_order)
