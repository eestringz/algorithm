
import sys

input = sys.stdin.readline

T = int(input())
dp = [[0, 0] for _ in range(100001)]
dp[1] = [1, 0]
dp[2] = [1, 1]
dp[3] = [2, 2]

for n in range(4, 100001):
    dp[n][0] = (dp[n - 3][1] + dp[n - 2][1] + dp[n - 1][1]) % 1000000009
    dp[n][1] = (dp[n - 3][0] + dp[n - 2][0] + dp[n - 1][0]) % 1000000009

for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])
