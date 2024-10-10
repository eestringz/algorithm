import sys

input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]  # dp[i][j]는 i개의 W, j개의 H를 가지는 경우의 수

for i in range(1, 31):
    dp[i][0] = 1

for i in range(1, 31):
    for j in range(1, 31):
        if j <= i:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

while True:
    N = int(input())
    if N == 0: break
    print(dp[N][N])
