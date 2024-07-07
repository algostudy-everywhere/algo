## 완주하지 못한 선수


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    flag=0
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            answer=participant[i]
            flag=1
            break
            
    if flag==0:
        answer=participant[-1]
        
        
    
    return answer


## 햄버거 만들기


def solution(ingredient):
    answer = 0
    
    stack=[]

    for i in ingredient:
        if stack and stack[-1]==1 and len(stack)>=4:

            if stack[-4:-1]==[1,2,3]:
                answer+=1
                for j in range(4):
                    stack.pop()
                
                
        stack.append(i)
    
    if stack and stack[-1]==1 and len(stack)>=4:
        if stack[-4:-1]==[1,2,3]:
                answer+=1
                for j in range(4):
                    stack.pop()
        
    
    
    
    return answer

## 구명보트


def solution(people, limit):
    answer = 0
    people.sort()
    a=0
    b=len(people)-1
    while a<b:
        if people[a]+people[b]<=limit:
            a+=1
            answer+=1
        b-=1

            

    return len(people)-answer