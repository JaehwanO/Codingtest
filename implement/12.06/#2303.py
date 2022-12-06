from itertools import combinations

n = int(input())
tmp = []
for _ in range(n):
    m = 0
    cards = list(map(int,input().split()))
    for c in combinations(cards,3):
        m = max(m,sum(c)%10)
    tmp.append(m)
ans_m = max(tmp)
ans = []
for i,num in enumerate(tmp):
    if num == ans_m:
        ans.append(i+1)

print(ans[-1])
