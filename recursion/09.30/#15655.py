n, m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
s = []

def back(r):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(r,len(l)):
        if len(s)>0:
            if l[i] not in s and s[-1]<=l[i]:
                s.append(l[i])
                back(r+1)
                s.pop()
        else:
            if l[i] not in s:
                s.append(l[i])
                back(r+1)
                s.pop()
           

back(0)