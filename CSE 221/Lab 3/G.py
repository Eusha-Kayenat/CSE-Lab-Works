def post_order(in_ord, pre_ord, in_start, in_end, pre_idx):
    if in_start > in_end or pre_idx[0] >= len(pre_ord):
        return
    
    r = pre_ord[pre_idx[0]]
    pre_idx[0] += 1

    r_index = in_ord.index(r, in_start, in_end + 1)
    post_order(in_ord, pre_ord, in_start, r_index - 1, pre_idx)
    post_order(in_ord, pre_ord, r_index + 1, in_end, pre_idx)
    
    postorder.append(r)

def solve():
    n = int(input())
    in_ord = list(map(int, input().split()))
    pre_ord = list(map(int, input().split()))
    
    global postorder
    postorder = []
    pre_idx = [0]  
    
    post_order(in_ord, pre_ord, 0, n - 1, pre_idx)
    
    print(*postorder)

solve()
