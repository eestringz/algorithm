def solution(numbers, target):
    q = [0]
    
    for num in numbers:
        temp = []
        for qq in q:
            temp.append(qq + num)
            temp.append(qq - num)
            
        q = temp
    
    return q.count(target)
