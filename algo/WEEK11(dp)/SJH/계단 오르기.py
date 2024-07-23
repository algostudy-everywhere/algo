
n=int(input())
dp=[0]*(n+1)

stair=[0]
for i in range(n):
    stair.append(int(input()))

dp[1]=stair[1]
if n>1:
    dp[2]=max(dp[1]+stair[2],stair[2]+dp[0])

    for i in range(3,n+1):
        dp[i]=max(dp[i-2]+stair[i],dp[i-3]+stair[i]+stair[i-1])


print(dp[n])
