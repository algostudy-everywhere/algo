import sys

input = sys.stdin.readline

n = int(input())

triangle = []

for _ in range (n):
    compo = list(map(int, input().split()))
    triangle.append(compo)
    
for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
answer = max(triangle[n-1])
    
print(answer)