n = int(input())

dp = [1, 1, 0, 1, 1] + [0] * (n - 4)

for i in range(5, n + 1):
    if dp[i - 1] == 0 or dp[i - 3] == 0 or dp[i - 4] == 0:
        dp[i] = 1

if dp[n] == 1:
    print("SK")
else:
    print("CY")