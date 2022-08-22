import math

m = int(input())
n = int(input())
a = int(math.sqrt(m))
b = int(math.sqrt(n))
# print(a)
l = []
for i in range(a,b+1):
    if i**2 >=m and i**2 <=n:
        l.append(i**2)
if l:
        
    print(sum(l))
    print(min(l))
else:
    print(-1)