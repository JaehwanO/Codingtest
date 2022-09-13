from itertools import combinations
import sys
input = sys.stdin.readline
n, s = map(int,input().split())
l = list(map(int,input().split()))
# print(l)
cnt = 0

for i in range(1,n+1):
    comb = combinations(l,i)
    for j in comb:
        if sum(j)==s:
            cnt +=1
            print(j)
print(cnt)