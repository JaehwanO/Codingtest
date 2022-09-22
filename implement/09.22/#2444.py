n = int(input())
t = ((2*n)-1)
s = (t//2)+1
for i in range(1,n+1):
    print(" "*(s-i) + "*"*((2*i)-1))
for i in range(n-1,0,-1):
    print(" "*(s-i) + "*"*((2*i)-1))
    