from collections import deque

a,b=map(int,input().split())
c=[i for i in range(1,a+1)]

result=[]
i=0
u=0

while c:
    for i in range(b-1):
        c.append(c.pop(0))
    result.append(str(c.pop(0)))


print("<"+",".join(result)+">")
