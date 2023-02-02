s = input()
ans = ''
for a in s:
    if a.upper()== a:
        ans += a.lower()
    else:
        ans += a.upper()
print(ans)