import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for i in range(1, n + 1):
    y, x, w, h = map(int, input().split())
    for r in range(y, y + w):
        arr[r][x:x+h] = [i]*h

for k in range(1, n + 1):
    cnt = 0
    for i in range(1001):
        cnt += arr[i].count(k)
    print(cnt)



# 아래는 처음 코드. 시간초과를 해결하기 위해 수정.

# n = int(input())
# arr = [[0] * 1001 for _ in range(1001)]
# for i in range(1, n + 1):
#     y, x, w, h = map(int, input().split())
#     for r in range(y, y + w):
#         for c in range(x, x + h):
#             arr[r][c] = i
# 
# for k in range(1, n + 1):
#     cnt = 0
#     for i in range(1001):
#         cnt += arr[i].count(k)
#     print(cnt)

