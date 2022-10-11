s = input()

stk = []
temp = 1
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        stk.append(s[i])
        temp *= 2
    elif s[i] == '[':
        stk.append(s[i])
        temp *= 3

    elif s[i] == ')':
        if not stk or stk[-1] == "[":
            ans = 0
            break
        if s[i-1] == '(':
            ans += temp
        stk.pop()
        temp //= 2
    
    else:
        if not stk or stk[-1] == "(":
            ans = 0
            break
        if s[i-1] == "[":
            ans += temp
        stk.pop()
        temp //= 3

if stk:
    print(0)
else:
    print(ans)