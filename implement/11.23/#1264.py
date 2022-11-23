vowels = ['a','e','i','o','u']
while 1:
    cnt = 0
    s = input()
    if s == '#':
        break
    for i in s:
        if i.lower() in vowels:
            cnt += 1
    print(cnt)
