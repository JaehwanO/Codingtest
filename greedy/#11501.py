T = int(input())

for _ in range(T):
    N = int(input())
    result = 0

    queue = list(map(int, input().split()))
    
    while True:
        if len(queue)==0:
            break
        
        num = queue.pop()

        for i in range(len(queue)-1,-1,-1):
            if num >= queue[i]:
                result += (num - queue[i])
                queue.pop()
            else: 
                break

    print(result)

# # import sys

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     price = list(input().split())
#     # print(price)
#     big = 0
#     big_list=[]
#     for i in range(len(price)):
#         big = 0
#         for j in range(i+1,len(price)):
#             if int(price[j])-int(price[i]) >= 0:
#                 big = max(big,int(price[j])-int(price[i]))
#             else:
#                 big = 0
#         big_list.append(big)
#     print(sum(big_list))
    
#     # n = int(sys.stdin.readline().rstrip())
