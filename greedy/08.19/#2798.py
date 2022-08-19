import sys

n,m = map(int, sys.stdin.readline().split())

bj = 0

lst = list(map(int, sys.stdin.readline().split()))

num = 0

sub=[]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            bj = bj + lst[i] + lst[j] + lst[k]
            diff = m - bj
            if diff >= 0 and m - num >= diff:
                num = bj
            bj = 0

print(num)