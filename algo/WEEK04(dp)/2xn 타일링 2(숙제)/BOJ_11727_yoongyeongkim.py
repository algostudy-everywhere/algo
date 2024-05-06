# 문제 이름 : 2xn 타일링 2
# 문제 링크 : https://www.acmicpc.net/problem/11727
# 풀이 노트 : https://www.notion.so/do-yoongyo2/BOJ_11727_2xn-2-7b89bb451f404cde84377d9792dede5b?pvs=4
#
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

n = int(input())
result = [0] * 1001

result[1] = 1
result[2] = 3

for i in range(3, n+1):
    if n < 3:
        break
    result[i] = result[i-1] + (result[i-2] * 2)

print(result[n] % 10007)