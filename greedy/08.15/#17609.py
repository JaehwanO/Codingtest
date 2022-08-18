import sys

def ispseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def ispalindrome(word, left, right):
    if word == word[::-1]:
        return 0
    else:
        while left < right:
            if word[left] != word[right]:
                check_left = ispseudo(word, left + 1, right)
                check_right = ispseudo(word, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T):
    word = sys.stdin.readline().rstrip("\n")
    left, right = 0, len(word)-1
    answer = ispalindrome(word, left, right)
    print(answer)


# from collections import deque

# T = int(input())
# for _ in range(T):
#     word = str(input())
#     my_list = list(word)
#     dq = deque(my_list)
#     cnt = 0
#     while len(dq) != 0:        
#         if cnt == 2:
#             break
#         elif dq[0] == dq[-1]:
#             print(dq[0],dq[-1])
#             dq.pop()
#             dq.popleft()
#         # print(dq)
#         elif dq[0] == dq[-2]:
#             dq.pop()
#             cnt += 1
#         elif dq[1] == dq[-1]:
#             dq.popleft()
#             cnt += 1
#         elif dq[0] != dq[-1]:
#         # dq.pop()
#         # dq.popleft()
#             cnt += 2
#     print(cnt)
