n = int(input())

for _ in range(n):
    a = list(map(int,input().split()))
    a.sort()
    print(a[-3])