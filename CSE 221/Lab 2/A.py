N,S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = N-1
while start < end:
    sum=arr[start] + arr[end]
   
    if sum ==S:
        print(start + 1, end + 1)
        break
    elif sum<S:
        start += 1
    else:
        end -= 1
else:
    print(-1)
