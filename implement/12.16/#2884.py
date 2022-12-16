h,m = map(int,input().split())
new = h*60 + m - 45
print((24+new//60)%24, new%60)