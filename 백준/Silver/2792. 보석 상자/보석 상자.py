import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for _ in range(M):
    lst.append(int(input()))

s = 1
e = max(lst)

while s <= e:
    mid = (s + e) // 2
    student_cnt = 0
    for n in lst:
        if n % mid == 0:
            student_cnt += n // mid
        else:
            student_cnt += n // mid + 1

    if student_cnt > N:
        s = mid + 1
    else:
        e = mid - 1

print(s)
