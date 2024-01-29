import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int,input().split())
d = defaultdict(list )
for _ in range(n):
    name = input().rstrip()
    num = int(input())
    for _ in range(num):
        member = input().rstrip()
        d[name].append(member)
    d[name].sort()

for _ in range(m):
    c = input().rstrip()
    q = int(input())
    if q:
        for key,value in d.items():
            if c in value:
                print(key)
    else:
        for ppl in d[c]:
            print(ppl)
