import sys

n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

visited=[0]*(n+1)
ans=sys.maxsize

def dfs(start,depth):
    global ans
    if depth==(n//2):
        a,b=0,0
        for i in range(n):
            for j in range(i+1,n):
                if visited[i] and visited[j]:
                    a+=(graph[i][j]+graph[j][i])
                elif not visited[i] and not visited[j]:
                    b+=(graph[i][j]+graph[j][i])

        ans=min(ans,abs(a-b))
                    
    for i in range(start,n):
        if visited[i]==0:
            visited[i]=1
            dfs(depth+1,start+1)
            visited[i]=0

            
dfs(0,0)
print(ans)


        
    
