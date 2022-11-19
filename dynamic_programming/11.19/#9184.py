#dict사용
dict1 = {}
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    elif (a,b,c) in dict1:
        return dict1[a,b,c]
    elif a < b and b < c:
        dict1[a,b,c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dict1[a,b,c]
    else:
        dict1[a,b,c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dict1[a,b,c]
a = 0
b = 0
c = 0
while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print('w({}, {}, {}) = {}'.format(a,b,c,w(a,b,c)))