n=int(input())
ans=0
row=[0]*n


def queen(x):
    for i in range(x):
        if row[x]==row[i] or abs(x-i)==abs(row[x]-row[i]):
            return False
    return True


def dfs(x):
    global ans
    if x==n:
        ans+=1
        return
    else:
        for i in range(n):
            row[x]=i
            if queen(x):
                dfs(x+1)
dfs(0)
print(ans)
