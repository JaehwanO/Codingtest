x = int(input())
n = int(input())
total = 0

for _ in range(n):
    a,b = map(int,input().split())
    total += a*b

if x == total:
    print("Yes")
else:
    print("No")
