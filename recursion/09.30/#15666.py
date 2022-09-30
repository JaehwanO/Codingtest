n, m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
s = []
ans = []
visited = [False]*(n+1)

def back():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    overlap = 0
    for i in range(len(l)):
        if overlap != l[i] :
            if len(s)>0:
                if s[-1] <= l[i]:
                    s.append(l[i])
                    overlap = l[i]
                    # visited[i] = True
                    back()
                    s.pop()
                    # visited[i] = False
            else:
                s.append(l[i])
                overlap = l[i]
                # visited[i] = True
                back()
                s.pop()
                # visited[i] = False

back()