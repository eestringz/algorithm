import sys

input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for weight, value in items:
    # 무게 제한부터 역순으로 순회
    for current_weight in range(K, weight - 1, -1):
        dp[current_weight] = max(dp[current_weight], dp[current_weight - weight] + value)

print(dp[K])
