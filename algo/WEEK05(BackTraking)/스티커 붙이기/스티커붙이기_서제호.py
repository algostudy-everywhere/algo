n,m,k=map(int,input().split())


def check(onebon,sticker):
    r=len(sticker)
    c=len(sticker[0])
    for x in range(r):
        for y in range(c):
            if onebon[x+i][y+j]+sticker[x][y]>1:
                return False
    return True

def do90(sticker):
    r=len(sticker)
    c=len(sticker[0])
    new_sticker=[[0]*r for i in range(c)]
    
    for i in range(c):
        for j in range(r):
            new_sticker[i][j]=sticker[r-j-1][i]
    return new_sticker

def attach(a,sticker):
    r=len(sticker)
    c=len(sticker[0])
    for x in range(r):
        for y in range(c):
            a[x+i][y+j]+=sticker[x][y]
    return 
    
            
onebon=[[0]*m for i in range(n)]
                   
for t in range(k):
    a,b=map(int,input().split())
    sticker=[list(map(int,input().split())) for i in range(a)]
    visited=False
    cnt=0
    while cnt<4:
        if visited==True:
            break
        for i in range(n-len(sticker)+1):
            if visited==True:
                break
            for j in range(m-len(sticker[0])+1):
                if check(onebon,sticker):
                    attach(onebon,sticker)
                    visited=True
                    break
        sticker=do90(sticker)
        cnt+=1

ans=0

for i in range(n):
    for j in range(m):
        ans+=onebon[i][j]

print(ans)


        
