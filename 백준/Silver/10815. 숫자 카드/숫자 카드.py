import sys

input = sys.stdin.readline

n = int(input())
card = set(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

for i in range(m):
    if lst[i] in card:
        print(1, end=' ')
    else:
        print(0, end=' ')