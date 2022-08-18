n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
s = 0
print(a)
for i in range(n):
    s += (a.pop()*b.pop())
print(s)