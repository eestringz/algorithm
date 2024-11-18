import sys

input = sys.stdin.readline

N, M = map(int, input().split())
min_s, min_e = 1000, 1000
for _ in range(M):
    s, e = map(int, input().split())
    min_s, min_e = min(min_s, s), min(min_e, e)

acc = 100000  # 최대 지출액
cnt_s = (N // 6 + 1)  # 구입할 6개입 세트의 개수
if N % 6 == 0:
    cnt_s -= 1

while cnt_s >= 0:
    cnt_e = N - cnt_s * 6 if N - cnt_s * 6 > 0 else 0  # 구입할 낱개의 개수
    acc = min(min_s * cnt_s + min_e * cnt_e, acc)

    cnt_s -= 1

print(acc)
