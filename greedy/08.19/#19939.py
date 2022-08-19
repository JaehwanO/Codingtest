def solution():
    n, k = map(int, input().split())
    sum_minimum = k*(k+1)//2
    if sum_minimum > n:
        return -1
    if (n-sum_minimum) % k == 0:
        return k-1
    else:
        return k
print(solution())



# from itertools import combinations

# n,k = map(int,input().split())
# l=[]
# for _ in range(1,n+1):
#     l.append(_)
# # print(l)
# my = []
# new = (list(combinations(l,k)))
# for i in range(len(new)):
#     if sum(new[i]) == n:
#         my.append(new[i])
        
#     # print(sum(new[i])
# my.sort(reverse=True)
# if my:
#     print(max(my[0])-min(my[0]))
# else:
#     print(-1)


# # k개의 수를 더서 n을 만들 수 있냐 없냐
