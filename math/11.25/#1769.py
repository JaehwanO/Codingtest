x = input()

cnt = 0
while len(x) > 1:
    tmp = 0
    cnt += 1
    for i in x:
        tmp += int(i)
    x = str(tmp)
    # print(x)


y = int(x)
print(cnt)
if y%3 == 0:
    print("YES")
else:
    print("NO")