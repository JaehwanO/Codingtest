n, m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
s = []

def back():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in l:
        if len(s)>0:
            if s[-1]<=i:
                s.append(i)
                back()
                s.pop()
        else:
            s.append(i)
            back()
            s.pop()
back()