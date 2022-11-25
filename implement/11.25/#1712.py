a,b,c = map(int,input().split())
if c-b != 0 and c>b:
    ans = a//(c-b)+1
    print(ans)
else:
    print(-1)
