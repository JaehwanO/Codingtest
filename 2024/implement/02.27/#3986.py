import sys
input = sys.stdin.readline

n = int(input())

cnt = 0 

for _ in range(n):
    s = input().rstrip()

    l = []

    for i in range(len(s)):
        if l and l[-1] == s[i]:
            l.pop()
        else:
            l.append(s[i])

    if not l:
        cnt +=1

print(cnt)