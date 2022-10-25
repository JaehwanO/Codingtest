def rotate(number,direct):
    if direct:
        wheels[number].appendleft(wheels[number].pop())
    else:
        wheels[number].append(wheels[number].popleft())


def check(w,d): 
    is_rotate = [False for _ in range(4)]
    is_rotate[w] = True
    for i in range(w-1,-1,-1):
        if wheels[i][2] != wheels[i+1][-2]:
            is_rotate[i] =True
        else:
            break
    for i in range(w+1,4):
        if wheels[i][-2] != wheels[i-1][2]:
            is_rotate[i] = True
        else:
            break
    for i in range(4):
        if is_rotate[i] and (w-i)%2 == 0:
            rotate(i,d)
        elif is_rotate[i] and (w-i)%2 == 1:
            rotate(i,not d)

from collections import deque
wheels = []
for _ in range(4):
    wheel = deque(list(input()))
    wheels.append(wheel)

K = int(input())
for _ in range(K):
    a,b = map(int,input().split()) # 휠, 방향
    if b == 1:
        is_right = True
    else:
        is_right = False
    check(a-1,is_right)

result = 0
for i in range(4):
    result+= int(wheels[i][0])*(2**i)

print(result)


# import sys
# from collections import deque


# def right(s):
#     s = s[-1]+s[:-2]
#     return s

# def left(s):
#     s = s[1:] + s[0]
#     return s

# def check1(a,b):
#     if a[2]==b[-2]:
#         return False
#     else:
#         return True

# def check2(a,b):
#     if a[-2]==b[-2]:
#         return False
#     else:
#         return True

# input = sys.stdin.readline
# gear = [''] + [input().rstrip() for _ in range(4)]
# # print(gear)

# k = int(input())
# for _ in range(k):
#     turn = [False] * (5)
#     x,y = map(int,input().split())
#     turn[x] = True

#     if x == 1:
#         turn[x+1] = check1(gear[x],gear[x+1])
#     elif x == 2:
#         turn[x-1] = check2(gear[x-1],gear[x])
#         turn[x+1] = check1(gear[x],gear[x+1])
#     elif x == 3:
#         turn[x+1] = check1(gear[x],gear[x+1])
#         turn[x-1] = check2(gear[x-1],gear[x])
#     elif x == 4:
#         turn[x-1] = check2(gear[x-1],gear[x])
#     print(turn)