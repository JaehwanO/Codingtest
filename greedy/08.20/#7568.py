n = int(input())
l = []
ans = []
for _ in range(n):
    l.append(list(map(int,input().split())))

for i in range(n):
    count = 0
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            count += 1
    ans.append(count +1)
for d in ans:
    print(d,end=" ")
