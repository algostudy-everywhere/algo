n, m = map(int, input().split())
numbers = []

def solution(n: int, m: int):
    if len(numbers) >= m:
        print(' '.join(map(str, numbers)))
        return

    for k in range(1, n + 1):
        if k in numbers:
            continue
        else:
            numbers.append(k)
            solution(n, m)
            numbers.pop()

solution(n, m)