from itertools import permutations

def sosu(u):
    if u<2:
        return False
    for i in range(2,u):
        if u%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    result = set()
    for i in range(1,len(numbers)+1):
        a=list(permutations(numbers,i))
        for i in a:
            b="".join(i)

            if sosu(int(b)):
                result.add(int(b))
                

    return len(result)
