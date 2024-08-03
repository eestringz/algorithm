def dfs(x, y, lev):
    if x == y:
        return lev

    for it in lst[x]:
        if used[it] != 1:
            used[it] = 1
            ret = dfs(it, y, lev + 1)
            if ret != -1:
                return ret
            used[it] = 0

    return -1


n = int(input())
x, y = map(int, input().split())
m = int(input())
lst = [[]] + [[] for _ in range(n)]
used = [0] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)
    lst[e].append(s)

used[x] = 1
ans = dfs(x, y, 0)
print(ans)
