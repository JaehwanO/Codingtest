n,l = map(int,input().split())
L = str(l)
cnt = 0
num = 0
while cnt != n:
    num += 1
    if L in str(num):
        continue
    cnt += 1

print(num)