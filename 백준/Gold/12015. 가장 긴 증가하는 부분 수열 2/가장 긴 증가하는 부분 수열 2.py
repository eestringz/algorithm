import sys

input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
ans = [0]   # 가장 긴 증가하는 부분 수열을 저장할 리스트를 초기화

for i in range(1, n + 1):
    if lst[i] > ans[-1]:
        ans.append(lst[i])
    else:
        # 이진 탐색을 사용하여 현재 원소를 적절한 위치에 추가.
        # 만약 더 작은 수로 증가수열을 만들 수 있다면 마지막 원소를 더 작은 수로 교체. (뒤에 더 많은 값을 담을 수 있으므로.)
        s, e = 0, len(ans) - 1
        while s < e:
            mid = (s + e) // 2
            if ans[mid] < lst[i]:
                s = mid + 1
            else:
                e = mid
        ans[e] = lst[i]

print(len(ans) - 1)