n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

def dfs(depth,s):
    
    if depth==m:
        print(*s)
        return

    re=0
    for i in a:
        if i!=re:
            re=i
            s.append(i)
            dfs(depth+1,s)
            s.pop()

            
dfs(0,[])
