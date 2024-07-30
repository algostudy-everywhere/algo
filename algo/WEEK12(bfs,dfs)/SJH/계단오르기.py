import sys
from collections import deque
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]


graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))


dp=[[-1]*m for i in range(n)]
dp[0][0]=1
def dfs(x,y):
    global dp
    if dp[x][y]==-1:
        dp[x][y]+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[x][y]<graph[nx][ny]:
                    dp[x][y]+=dfs(nx,ny)
    return dp[x][y]
                
    

result=dfs(n-1,m-1)
print(result)

    

