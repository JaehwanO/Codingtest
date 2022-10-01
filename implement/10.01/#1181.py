n = int(input())
l = []
s = [[]*51 for i in range (51)]
for _ in range(n):
    l.append(input())

for i in l:
    if i not in s[len(i)]:
        s[len(i)].append(i)
        s[len(i)].sort()
for j in s:
    if j:
        for k in j:
            print(k)