n, l = map(int, input().split())
my = list(map(int,input().split()))
my.sort()
for i in my:
    if i <= l:
        l += 1
print(l)