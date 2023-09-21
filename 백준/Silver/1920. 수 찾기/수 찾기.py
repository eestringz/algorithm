import sys

input = sys.stdin.readline

n = int(input())
sett = set(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

for i in range(m):
    if lst[i] in sett:
        print(1)
    else:
        print(0)