n = int(input())
a = list(map(int, input().split()))
b = a[::-1]

dph = [1 for i in range(n)]
dpl = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dph[i] = max(dph[i],dph[j]+1)

        if b[i] > b[j]:
            dpl[i] = max(dpl[i],dpl[j]+1)
            
m = 0
for i in range(n):
    m = max(m,dph[i]+dpl[n-i-1]-1) 
print(m)