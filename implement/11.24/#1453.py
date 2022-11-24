n = int(input())
a = list(map(int,input().split()))
s = []
cnt = 0
for i in a:
    if i in s:
        cnt += 1
    else:
        s.append(i)
print(cnt)