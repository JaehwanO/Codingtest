# 멀티탭 스케줄링
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
use = list(map(int, input().split()))

plugs = []
result = 0
for i in range(K):
    # 이미 있다면
    if use[i] in plugs:
        continue

    # 빈공간이 있다면
    if len(plugs) != N:
        plugs.append(use[i])
        continue

    # 가장 멀리 있는 플러그의 인덱스
    far_one = 0
    temp = 0
    # 현재 꽂혀있는 플러그들 확인
    for plug in plugs:
        # 앞으로 사용할 플러그에 없으면
        if plug not in use[i:]:
            temp = plug
            break
        # 현재까지 가장 멀리 있는 플러그보다 멀리 있으면
        elif use[i:].index(plug) > far_one:
            far_one = use[i:].index(plug)
            temp = plug
    plugs[plugs.index(temp)] = use[i]
    result += 1

print(result)

# from collections import defaultdict

# n, k = map(int,input().split())
# l = list(map(int,input().split()))

# d = defaultdict(int)
# for i in range(k):
#     d[l[i]] += 1

# # print(d)

# plugged = []

# ans = 0
# for i in l:
#     d[i] -= 1
#     if i not in plugged and len(plugged) < n:
#         plugged.append(i)
#         # d[i] -= 1

#     elif i not in plugged and len(plugged) == n:
#         #뭘 뺄지 결정
#         smallest_used = 1000000
#         for j in plugged:
#             if d[j] <= smallest_used:
#                 smallest_item = j
#                 smallest_used = d[j]

#         plugged.remove(smallest_item)
#         plugged.append(i)
#         ans += 1

# print(ans)