import sys

input = sys.stdin.readline


def dfs(n, cnt):
    global ans

    # 끝까지 진행해도 결과 갱신 불가능.(가지치기)
    if ans >= cnt + (N - n) * 2:  # cnt + (N-n)*2 는 결과 최댓값
        return

    if n == N:  # 모든 계란을 들고 부딪히기 완료
        ans = max(ans, cnt)
        return

    if arr[n][0] <= 0:  # 현재 계란이 이미 깨진 경우 -> 다음 계란으로.
        dfs(n + 1, cnt)
    else:  # 현재 계란이 안깨진 상태
        flag = 0  # 한 번도 안 부딪혔어도 다음 계란으로 가야함.
        for j in range(N):  # 하나씩 부딪혀보기.
            if j == n or arr[j][0] <= 0: continue
            arr[j][0] -= arr[n][1]
            arr[n][0] -= arr[j][1]
            flag = 1
            dfs(n + 1, cnt + int(arr[j][0] <= 0) + int(arr[n][0] <= 0))
            arr[j][0] += arr[n][1]  # 리턴 후 원상 복구
            arr[n][0] += arr[j][1]
        if flag == 0:
            dfs(n + 1, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 계란 index, 깨진 계란 개수
dfs(0, 0)
print(ans)