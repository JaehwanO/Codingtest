d = {'-':0, '\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/':-1,}

while True:
    ans = 0
    s = input()
    if s == '#':
        break
    for i in range(len(s)):
        ans += d[s[i]]*(8**(len(s)-1-i))
    print(ans)
