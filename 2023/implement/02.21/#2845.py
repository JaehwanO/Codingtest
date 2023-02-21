l,p = map(int,input().split())
total = l*p
ppl = list(map(int,input().split()))
ans = []
for i in ppl:
    ans.append(i-total)
print(*ans)