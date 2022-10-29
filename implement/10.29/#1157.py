from collections import defaultdict

d = defaultdict(int)
s = input()
for i in s:
    d[i.upper()] += 1

m = max(d.values())
ans = []
for k,v in d.items():
    if v == m:
        ans.append(k)

if len(ans) == 1:
    print(ans[0])
else:
    print("?")
