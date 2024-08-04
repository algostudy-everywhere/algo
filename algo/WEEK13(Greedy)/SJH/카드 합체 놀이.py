from  heapq import heapify,heappush,heappop

n,m=map(int,input().split())
a=list(map(int,input().split()))

heap=[]

heapify(a)
for i in range(m):
    c=heappop(a)
    d=heappop(a)
    e=c+d
    heappush(a,e)
    heappush(a,e)
print(sum(a))


    
