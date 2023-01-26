while True:
    a = list(map(int,input().split()))
    if len(a) == 1 and a[0] == 0:
        break
    n = a[0]
    a = a[1:]
    ans = ["$"]
    while a:
        if ans[-1] != a[-1]:
            ans.append(a.pop())
        else:
            a.pop()
    print(*ans[::-1])