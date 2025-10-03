import sys
input=sys.stdin.readline

n,m=map(int,input().split())
E=[]
for _ in range(m):
    u,v,w=map(int,input().split())
    E.append((w,u,v))
E.sort()

p=list(range(n+1))
sz=[1]*(n+1)
def f(x):
    while p[x]!=x:
        p[x]=p[p[x]]
        x=p[x]
    return x

ans=0; edges=0
for w,u,v in E:
    a,b=f(u),f(v)
    if a!=b:
        if sz[a]<sz[b]: a,b=b,a
        p[b]=a; sz[a]+=sz[b]
        ans+=w; edges+=1
        if edges==n-1: break
print(ans)
