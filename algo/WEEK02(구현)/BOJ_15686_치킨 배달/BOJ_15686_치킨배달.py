from itertools import combinations
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]

house=[]
chi=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]==1:
            house.append([i,j])
        elif graph[i][j]==2:
            chi.append([i,j])



answer=sys.maxsize
for i in combinations(chi,m):
    temp=0
    for k in house:
        a,b=k
        result=sys.maxsize
        for j in range(m):
            x,y=i[j]
            result=min(result,abs(a-x)+abs(b-y))
        temp+=result
    answer=min(temp,answer)
print(answer)
