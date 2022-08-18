import sys
import heapq

n = int(sys.stdin.readline())
ab = []
[heapq.heappush(ab, list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
l, p = map(int, sys.stdin.readline().split())
cnt = 0
heap = []

# 현재 있는 연료로 마을까지 갈수 있을 때까지 반복
while p < l:

    # 앞으로 주유소가 있고 다음 주유소를 현재 연료로 갈 수 있으면 
    # 현재 연료로 갈 수 있는 모든 주유소를 확인
    while ab and ab[0][0] <= p:
        # 주유소의 연료양 기준으로 최대힙을 만들어 리스트에 푸시한다.
        a, b = heapq.heappop(ab)
        heapq.heappush(heap, [-b, a])

    # 현재 연료로 다음 주유소까지 갈 수 없으므로 -1 출력
    if not heap:
        cnt = -1
        break
    # print(heap)

    # 최대힙을 팝한다.(연료를 제일 많이 충전해주는 주유소)
    b, a = heapq.heappop(heap)
    # print(b,a)
    # 연료를 충전한다.
    p += -b
    cnt += 1

print(cnt)


# from re import A
# import sys
# from collections import deque
# N = int(input())
# a = deque()
# b = deque()
# for _ in range(N):
#     x, y =(map(int,sys.stdin.readline().split()))
#     a.append(x)
#     b.append(y)
# L, P = map(int,sys.stdin.readline().split())
# cnt = 0
# d = 0 #온 거리
# if P < b[0]:
#     print(-1)
# else:
#     d = a[0]
#     P -= a[0]
# while len(a)>1:
#     if P >= a[1]-a[0]:
#         d = a[1]
#         P -= (a[1]-a[0])
#         a.popleft()
#         b.popleft()
#     elif P < a[1]-a[0]:
#         cnt += 1
#         P += b[0]
# # print(d, P) #마지막에 막 도달했을 때 남은 연료, 아직 충전 안함
# # print(cnt)
# if d+P >= L or d+P+b[0] >=L:
#     print(cnt+1)
# else:
#     print(-1)
# # print(a) 
# # print(b)
        
    