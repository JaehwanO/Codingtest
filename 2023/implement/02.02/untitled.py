data =  list(map(int,input('숫자로만 이루어진 문자열을 입력하세요.')))
ans = 1
for num in data:
    if num:
        ans *= num
print(ans)
