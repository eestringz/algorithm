import sys

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
stack = []
ans = []
for i in range(1, n + 1):
    if not stack or stack[-1] < lst[0]:
        stack.append(i)
        ans.append('+')
    while stack and stack[-1] == lst[0]:
        stack.pop()
        lst.pop(0)
        ans.append('-')

if stack:
    print('NO')
else:
    print(*ans, sep='\n')