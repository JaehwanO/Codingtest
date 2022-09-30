n, m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
s = []
ans = []
# visited = [False]*(n+1)

def back():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    overlap = 0
    for i in range(len(l)):
        if overlap != l[i]:
            s.append(l[i])
            overlap = l[i]
            back()
            s.pop()
            

back()