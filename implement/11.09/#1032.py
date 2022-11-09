n = int(input())
l = []
for _ in range(n):
    l.append(input())

ans = list(l[0])

for i in range(n):
    for j in range(len(ans)):
        if ans[j] == l[i][j]:
            continue
        else:
            ans[j] = "?"
print(''.join(ans))