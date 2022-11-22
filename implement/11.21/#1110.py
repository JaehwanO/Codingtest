s = str(input())
z = s
cnt = 0
while True:

    if len(s) < 2:
        s = s.zfill(2)
    
    a,b = int(s[0]), int(s[1])
    c = str(a + b)
    tmp = str(b) + c[-1]
    if int(z) == int(tmp):
        break

    else:
        cnt += 1
        s = tmp
    
print(cnt+1)