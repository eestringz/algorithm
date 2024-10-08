import sys

input = sys.stdin.readline

tc = 1

while True:
    N = int(input())
    if N == 0: break

    manito = dict()  # 마니또 상태
    used = set()  # 중복체크
    cnt = 0  # 연결고리 개수

    for _ in range(N):
        s, e = input().split()
        manito[s] = e

    for key in manito:
        if key in used: continue
        used.add(key)
        value = manito[key]
        while True:
            used.add(value)
            if value == key:
                cnt += 1
                break
            else:
                value = manito[value]

    print(f'{tc} {cnt}')
    tc += 1
