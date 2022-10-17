def back():
    if len(s) == n:
        print(' '.join(map(str,s)))
        return 
    for i in range(1,k+1):
        if len(s)>0:
            if l[i]>=s[-1] and l[i] not in s :
                s.append(l[i])
                # visited[i] = True
                back()
                s.pop()
                # visited[i] = False
        else:
             if l[i] not in s:
                s.append(l[i])
                # visited[i] = True
                back()
                s.pop()
                # visited[i] = False

while True:
    l = list(map(int,input().split()))
    n = 6
    k = l[0]
    s = []
    visited = [False]*(k+1)
    if k == 0:
        break
    else:
        back()
        print()