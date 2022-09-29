from sys import stdin
import heapq


n, m = map(int, stdin.readline().split())

cards = [int(x) for x in stdin.readline().split()]
# cards 리스트를 heap으로 변환
heapq.heapify(cards)

for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))


# import sys
# from heapq import heappush, heapify
# input = sys.stdin.readline


# n, m = map(int,input().split())
# heap =[]
# l = list(map(int,input().split()))
# for i in l:
#     heappush(heap,i)
# for _ in range(m):
#     heap[0],heap[1] = heap[0]+heap[1],heap[0]+heap[1]
#     # print(heap)
# print(sum(heap))