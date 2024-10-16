def solution(arr):
    stack = []
    for num in arr:
        if len(stack) == 0:
            stack.append(num)
        else:
            if stack[-1] == num:
                continue
            else:
                stack.append(num)
                
    return stack