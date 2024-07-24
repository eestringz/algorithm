def solution(s):
    change_cnt = 0
    zero_cnt = 0

    while s != "1":
        change_cnt += 1
        num = s.count('1')
        zero_cnt += len(s) - num

        s = bin(num)[2:]

    return [change_cnt, zero_cnt]