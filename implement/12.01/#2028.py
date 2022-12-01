t = int(input())
for _ in range(t):
    s = int(input())
    length = len(str(s))
    n = str(s**2)
    if s == int(n[length*(-1):]):
        print("YES")
    else:
        print("NO")
