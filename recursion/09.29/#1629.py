from re import M


a,b,c = map(int,input().split())

def pow(a,b,c):
    # print(b)
    if b==1:
        return a%c
    val = pow(a,b//2,c)

    val = val * val % c
    # print(val)
    if b%2 == 0:
        return val
    return val*a%c
    
print(pow(a,b,c))
