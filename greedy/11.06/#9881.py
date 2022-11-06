n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()

ans = float('inf')
for i in range(100-16):
    tmp = 0 
    for j in range(n):
        if l[j] < i:
            tmp += (i-l[j]) * (i-l[j])
        if l[j] > i + 17:
            tmp += (l[j] - i -17)*(l[j] - i -17)
    ans = min(ans,tmp)
print(ans)