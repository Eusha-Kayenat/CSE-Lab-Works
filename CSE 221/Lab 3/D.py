mod = 10**9 + 7

def mat_multiply(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]
    ]
 
def mat_power(mat, power):
    res = [[1, 0], [0, 1]]  
    while power:
        if power % 2 == 1:
            res = mat_multiply(res, mat)
        mat = mat_multiply(mat, mat)
        power //= 2
    return res
 

t = int(input())
for _ in range(t):
    a11, a12, a21, a22 = map(int, input().split())
    x = int(input())
    A = [[a11, a12], [a21, a22]]
    Ax = mat_power(A, x)
    for row in Ax:
        print(*row)
