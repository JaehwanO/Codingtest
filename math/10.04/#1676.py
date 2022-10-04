n = int(input())
s = 1
for i in range(1,n+1):
    s *= i

s = str(s)[::-1]
cnt = 0

for i in s:
    if i == '0':
        cnt +=1
    else:
        break

print(cnt)