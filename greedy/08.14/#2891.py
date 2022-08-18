n ,s ,r = map(int,input().split())
a = list(input().split())
b = list(input().split())
# print(a)
# print(b)
for i in b:
    if i in a:
        a.remove(i)
        s -=1
    elif str(int(i)-1) in a:
        a.remove(str(int(i)-1))
        s -=1
        # print(a)
    elif str(int(i)+1) in a:
        a.remove(str(int(i)+1))
        s -=1
        # print(a)
    else:
        s -=0
print(s)