import sys
s, e, q = sys.stdin.readline().split()

s = int(s[:2]+s[3:])
e = int(e[:2]+e[3:])
q = int(q[:2]+q[3:])

d = set()
ans = 0

while True:
    try:
        t, n = sys.stdin.readline().split()
        t = int(t[:2]+t[3:])
        if t <= s:
            d.add(n)
        elif e<=t<=q and n in d:
            d.remove(n)
            ans += 1
    except:
        break

print(ans)