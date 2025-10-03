def res(a, b, mod):
    val = 1      
    a = a % mod     
    while b > 0:
        if b % 2 == 1: 
            val = (val * a) % mod       
        a = (a * a) % mod  
        b //= 2          
    return val
a, b= map(int, input().split())
print(res(a, b, 107))
