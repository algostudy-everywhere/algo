n,m=map(int,input().split())


def dfs(depth,s):
    if depth==m:
        print(*s)
        return
    else:
        for i in range(1,n+1):
            s.append(i)
            dfs(depth+1,s)
            s.pop()



dfs(0,[])
