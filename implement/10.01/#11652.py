m = int(input())
d = {}

for i in range(m):
    a = int(input())
    if a in d.keys():
        d[a] += 1
    else:
        d[a] = 1
    
    if i == 0:
        tmp = a
    if d[tmp] == d[a]:
        tmp = min(tmp,a)
    elif d[tmp] < d[a]:
        tmp = a
print(tmp)

