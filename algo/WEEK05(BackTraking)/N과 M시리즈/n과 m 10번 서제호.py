import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=[]
visited=[0]*n

def dfs(start,depth,s):
    if depth==m:
        print(*s)
        return
    remember=0
    for i in range(start,len(a)):
        if remember!=a[i]:
            s.append(a[i])
            remember=a[i]
            dfs(i+1,depth+1,s)
            s.pop()

dfs(0,0,[])

