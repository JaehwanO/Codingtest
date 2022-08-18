import sys
n ,m = map(int, sys.stdin.readline().split())
p =[]
s =[]
for _ in range(m):
    a ,b = map(int, sys.stdin.readline().split())
    p.append(a)
    s.append(b)
p_min = min(p)
s_min = min(s)
if p_min <= s_min * 6:
    answer = p_min * (n // 6) + s_min * (n % 6)
    if p_min < s_min * (n % 6):
        answer = p_min * (n//6 + 1)
else:
    answer = s_min * n

print(answer)