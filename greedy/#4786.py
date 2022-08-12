l, p , v = map(int, (input().split()))
count = 0

# if l == 0 and p==0 and v==0:

while v !=0:
    count += l * (v//p)
    v = v%p
    if v < p and v<l:
        count += v
        v -=v
    elif v < p and v>l:
        count += l
        v -= l
        break;
    
print(count)

# i = 0
# while True:
#     i+=1
#     l, p, v = map(int, input().split())
#     if l==0 and p==0 and v==0:
#         break
#     a = v//p
#     b = v%p
#     if l<b:
#         b = l
#     print("Case %d: %d" %(i, a*l+b))