n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

def dfs(start,depth,s):
    if depth==m:
        print(*s)
        return
    else:
        for i in range(start,len(a)):
            s.append(a[i])
            dfs(i+1,depth+1,s)
            s.pop()



dfs(0,0,[])
