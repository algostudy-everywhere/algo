n, m = map(int, input().split())
numbers = []

def solution(n: int, m: int):
    if len(numbers) >= m:
        print(' '.join(map(str, numbers)))
        return

    start = 1 if len(numbers) == 0 else numbers[-1] + 1

    for k in range(start, n + 1):
        numbers.append(k)
        solution(n, m)
        numbers.pop()

solution(n, m)