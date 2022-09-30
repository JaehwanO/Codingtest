n, m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
s = []

def back():
    if len(s)==m:
        print(' '.join(list(map(str,s))))
        return


    for i in l:
        if i not in s:
            s.append(i)
            back()
            s.pop()

back()