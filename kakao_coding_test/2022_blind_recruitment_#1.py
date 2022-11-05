def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def ten_to_n(n,k):
    tmp = ''
    while n > 0:
        n, mod = divmod(n,k)
        tmp += str(mod)
    return tmp[::-1]

def solution(n, k):
    ans = 0
    s = ten_to_n(n,k)
    # print(s)
    s = s.split("0")
    # print(s)
    for i in s:
        if i and is_prime(int(i)):
            ans += 1
    return ans
            
            
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num%i == 0:
#             return False 
#     return True

# def ten_to_n(n, k):
#     rev_base = ''

#     while n > 0:
#         n, mod = divmod(n, k)
#         rev_base += str(mod)

#     return rev_base[::-1] 


# def solution(n, k):
#     num = ten_to_n(n,k)
#     num_list = num.split('0')

#     cnt = 0
#     for i in num_list:
#         if i and is_prime(int(i)):
#                 cnt += 1
#     return cnt