import sys

input = sys.stdin.readline

T = int(input())
dp = [[0, 0, 0] for _ in range(100001)]

dp[1] = [1, 0, 0]  # 1의 분할 중 각각 1,2,3 으로 끝나는 경우의 수
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for n in range(4, 100001):
    dp[n][0] = (dp[n - 1][1] + dp[n - 1][2]) % 1000000009  # n의 분할 중 1로 끝나는 경우의 수
    dp[n][1] = (dp[n - 2][0] + dp[n - 2][2]) % 1000000009  # n의 분할 중 2로 끝나는 경우의 수
    dp[n][2] = (dp[n - 3][0] + dp[n - 3][1]) % 1000000009  # n의 분할 중 3로 끝나는 경우의 수

for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % 1000000009)
