def solution(n, lost, reserve):
    # 여벌 체육복이 있지만 도난당한 경우를 먼저 제거
    real_reserve = list(set(reserve) - set(lost))
    real_lost = list(set(lost) - set(reserve))
    
    lst = [1] * n
    for num in real_lost:
        lst[num - 1] = 0
    for num in real_reserve:
        lst[num - 1] += 1
    
    for i in range(n):
        if lst[i] == 0:
            if i > 0 and lst[i - 1] == 2:
                lst[i - 1] -= 1
                lst[i] += 1
            elif i < n - 1 and lst[i + 1] == 2:
                lst[i + 1] -= 1
                lst[i] += 1
                
    return n - lst.count(0)
