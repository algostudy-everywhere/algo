def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for i in numbers:
        tmp = []
        for j in leaves:
            tmp.append(j+i)
            tmp.append(j-i)
        leaves = tmp
        
    for leaf in leaves:
        if leaf == target:
            answer += 1
            
    return answer