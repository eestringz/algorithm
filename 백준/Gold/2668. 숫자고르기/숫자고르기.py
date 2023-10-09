import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(num):
    if used[num] == 0:
        used[num] = 1
        for x in lst[num]:
            top.add(num)
            bottom.add(x)
            if top == bottom:
                ans.extend(top)  # extend 를 사용하여 원소들만 담기
                return
            dfs(x)
    used[num] = 0


n = int(input())
lst = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    lst[i].append(int(input()))

ans = []  # 사이클인 정점들을 담기위한 리스트

used = [0] * (n + 1)
for i in range(1, n + 1):
    top = set()
    bottom = set()
    dfs(i)
    used[i] = 0
    
ans = sorted(list(set(ans)))
print(len(ans))
print(*ans, sep='\n')