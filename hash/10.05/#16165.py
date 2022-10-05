import sys
input = sys.stdin.readline

n, m = map(int,input().split())
s = {}
for _ in range (n):
    g_name = str(input().rstrip())
    number = int(input())
    s[g_name] = []
    for _ in range(number):
        m_name = str((input().rstrip()))
        s[g_name].append(m_name)

for i in range(m):
    name, num = input().rstrip(), int(input().rstrip())
    if num == 0:
        for n in sorted(s[name]):
            print(n)
    else:
        for g in s:
            if name in s[g]:
                print(g)