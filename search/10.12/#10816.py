n = int(input())
l = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))
l.sort()

def lower(target,len):
    st = 0
    en = len
    while (st < en):
        mid = (st+en)//2
        if l[mid] >= target:
            en = mid
        else:
            st = mid + 1
    return st

def upper(target,len):
    st = 0
    en = len
    while (st < en):
        mid = (st+en)//2
        if l[mid] > target:
            en = mid
        else:
            st = mid + 1
    return st


for i in num:
    print(upper(i,n) - lower(i,n))

# print(dict)