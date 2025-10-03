def mat_multiply(A, B, modu):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % modu, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % modu],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % modu, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % modu]
    ]

def mat_power(mat, pow, modu):
    res = [[1, 0], [0, 1]]
    while pow > 0:
        if pow % 2 == 1:
            res = mat_multiply(res, mat, modu)
        mat = mat_multiply(mat, mat, modu)
        pow //= 2
    return res
 
def sum_powers(a, n, m):
    if n == 0:
        return 0
    if a == 1:
        return n % m
    M = [[a % m, 1], [0, 1]]
    res = mat_power(M, n, m)
    return (res[0][1] * a) % m
 
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        a = int(data[idx])
        n = int(data[idx+1])
        m = int(data[idx+2])
        idx += 3
        results.append(str(sum_powers(a, n, m)))
    print('\n'.join(results))
 
if __name__ == "__main__":
    main()
