a, b = map(str,input().split())
l = []
for i in range(len(b)-len(a)+1):
    c = b[i:i+len(a)]
    cnt = 0
    for i in range(len(a)):
        if a[i] !=c[i]:
            cnt +=1
    l.append(cnt)
print(min(l))
        