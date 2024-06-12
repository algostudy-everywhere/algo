from collections import deque
def solution(priorities, location):
    answer = 0
    q=deque(priorities)
    name=deque()
    for i in range(len(priorities)):
        name.append(i)
    ans=name[location]
    
    while q:
        m=max(q)
        if q[0]<m:
            q.append(q.popleft())
            name.append(name.popleft())
        else:
            if ans==name[0]:
                answer+=1
                break
            else:
                q.popleft()
                name.popleft()
                answer+=1
        
        
        
    return answer
