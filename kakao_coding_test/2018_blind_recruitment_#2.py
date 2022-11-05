def convert(num,base):
    tmp = '0123456789ABCDEF'
    q,r = divmod(num,base)
    
    if q == 0:
        return tmp[r]
    else:
        return convert(q,base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    test = '' 
    for i in range(t*m):
        test += convert(i,n)
        
    while len(answer) < t:
        answer += test[p-1]
        p += m
    return answer
    # return answer