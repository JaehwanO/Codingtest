a,b = map(int,input().split())

print(max(int(str(a)[::-1]), int(str(b)[::-1])))