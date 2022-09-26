import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
s = []
ans = []


for i in range(n):
    while s:
        if s[-1][1] > l[i]:
            ans.append(s[-1][0]+1)
            break
        else:
            s.pop()
    if not s:
        ans.append(0)
    s.append([i,l[i]])
print(' '.join(map(str,ans)))