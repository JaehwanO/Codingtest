a,b = map(int,input().split())
r = 1
while(b!=a):
    r+=1
    temp = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if temp == b:
        print(-1)
        break
else:
    print(r)

# a, b = map(int,input().split())
# cnt = 1
# while b != a:
#     if str(b)[-1]=="1":
#         b = str(b)[:-1]
#         cnt += 1
#     elif int(b) < a:
#         cnt = -1
#         break
#     else:
#         b =int(b)
#         b = b//2
#         cnt +=1
# print(cnt)