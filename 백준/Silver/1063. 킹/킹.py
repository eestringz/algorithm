import sys

arr = [[0] * 8 for _ in range(8)]
lst = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

king, rock, N = sys.stdin.readline().split()

ky = ord(king[0]) - ord('A')
kx = int(king[1]) - 1
ry = ord(rock[0]) - ord('A')
rx = int(rock[1]) - 1

for _ in range(int(N)):
    st = sys.stdin.readline().strip()

    directy = [1, -1, 0, 0, 1, -1, 1, -1]   # lst와 index 맞추기
    directx = [0, 0, -1, 1, 1, 1, -1, -1]
    
    idx = lst.index(st)

    ky += directy[idx]
    kx += directx[idx]

    if ky < 0 or kx < 0 or ky > 7 or kx > 7:
        ky -= directy[idx]
        kx -= directx[idx]

    if ky == ry and kx == rx:

        ry += directy[idx]
        rx += directx[idx]

        if ry < 0 or rx < 0 or ry > 7 or rx > 7:
            ky -= directy[idx]   # rock의 배열범위가 벗어나면 king도 제자리로 돌아와야함.
            kx -= directx[idx]
            ry -= directy[idx]
            rx -= directx[idx]


print(chr(ky + ord('A')) + str(kx + 1))
print(chr(ry + ord('A')) + str(rx + 1))