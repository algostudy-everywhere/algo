import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+2)

dp[0] = 1
dp[1] = 2

for i in range(2,N+2):
    dp[i] = dp[i-2] + dp[i-1]


print(dp[N-1]%10007)