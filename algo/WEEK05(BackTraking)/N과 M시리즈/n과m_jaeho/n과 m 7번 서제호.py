n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

def dfs(depth,s):
    
    if depth==m:
        print(*s)
        return

    else:
        for i in a:
            s.append(i)
            dfs(depth+1,s)
            s.pop()

            
dfs(0,[])
