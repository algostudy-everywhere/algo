import sys

input = sys.stdin.readline

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            cnt += 1
            dfs(graph, i , visited)


N = int(input())
E = int(input())

cnt = 0 

graph = [[] for _ in range(N+1)]

visited = [False for _ in range(N+1)]


for i in range(E):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)
    
    
dfs(graph, 1, visited)

print(cnt)