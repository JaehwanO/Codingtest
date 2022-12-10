##
from collections import Counter
n = int(input())
ans = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    c = Counter(tmp)
    c = list(sorted(c.items(), key = lambda x : (x[1],x[0]), reverse=True))
    for num, freq in c:
        if freq == 1:
            ans.append(num*100)
            break
        if freq == 2:
            ans.append(1000+(num*100))
            break
        if freq == 3:
            ans.append(10000+(num*1000))
            break
print(max(ans))