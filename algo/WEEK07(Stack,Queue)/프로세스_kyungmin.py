from collections import deque
def search_max_priority(p):
    max_priority = 0
    for priority, _ in p:
        max_priority = max(priority, max_priority)
    return max_priority        
def solution(priorities, location):
    count = 0
    queue = deque([(priorities[i], i) for i in range(len(priorities))])
    while queue:
        max_priority = search_max_priority(queue)
        exe = queue.popleft()    
        if max_priority == exe[0]:
            count += 1
            if exe[1] == location:
                break
        else:
            queue.append(exe)
    return count
