n, m = map(int, input().split())
numbers = []
# n : 1~n
# m : 자릿수
# i : i번째(인덱스) 숫자 채울예정 -> 포인터 느낌 이자 numbers의 길이
# numbers: 지금까지 쌓은 숫자 리스트
def solution(n: int, m: int):
    if len(numbers) >= m:
        print(' '.join(map(str, numbers)))
        return

    for k in range(1, n + 1):
        numbers.append(k)
        solution(n, m)
        numbers.pop()

solution(n, m)