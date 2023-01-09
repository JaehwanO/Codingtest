k = int(input())
a = [1,0,1,1,2,3]
b = [0,1,1,2,3,5]

if k > 6:
    for i in range(5,k):
        a.append(a[i]+a[i-1])
        b.append(b[i]+b[i-1])
print(a[k],end = " ")
print(b[k])
