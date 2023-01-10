while True:
    s = list(input())
    if s[0] == '#':
        break
    ones = s.count('1')
    if s[-1] == 'e':
        if ones%2 == 0:
            s[-1] = '0'
        else:
            s[-1] = '1'
    if s[-1] == 'o':
        if ones%2 == 0:
            s[-1] = '1'
        else:
            s[-1] = '0'
    print(''.join(s))
    