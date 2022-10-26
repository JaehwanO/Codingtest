import sys
from collections import deque,Counter
input = sys.stdin.readline

n,k = map(int,input().split())
belt_up = deque(map(int,input().split()))
belt_down = deque()
for _ in range(n):
    belt_down.append(belt_up.pop())

robot = deque([False]*n) 
ans = 0

while True:
    #1단계
    #벨트 회전
    belt_up.appendleft(belt_down.popleft())
    belt_down.append(belt_up.pop())

    #로봇위치도 회전
    robot.pop()
    robot.appendleft(False)
    
    #2단계
    for i in range(n-1,-1,-1):
        if robot[i]:
            if i == n-1:
                robot[i] = False
            else:
                if robot[i+1] == False and belt_up[i+1] > 0:
                    robot[i] = False
                    robot[i+1] = True
                    belt_up[i+1] -= 1

                elif belt_up[i+1] <= 0:
                    robot[i] = True

    #3단계
    #비어있고, 위쪽 벨트 첫번째 내구도가 0 이상이면,
    if robot[0] == False and belt_up[0] > 0:
        #로봇추가
        robot[0] = True
        #내구도 1 감소
        belt_up[0] -= 1
    ans += 1
    #4단계
    s = belt_up.count(0) + belt_down.count(0)
    if s >= k:
        break

print(ans)

# import sys
# input = sys.stdin.readline
# from collections import deque

# n, k = map(int, input().split())
# belt = deque(list(map(int, input().split())))
# robot = deque([0]*n)
# res = 0

# while 1:
#     belt.rotate(1)
#     robot.rotate(1)
#     robot[-1]=0 #로봇이 내려가는 부분이니 0
#     if sum(robot): #로봇이 존재하면
#         for i in range(n-2, -1, -1): #현재자리에 로봇있고 다음자리에 없으며 내구도가 1이상
#             if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
#                 robot[i+1] = 1
#                 robot[i] = 0
#                 belt[i+1] -= 1
#         robot[-1]=0 #이 부분도 로봇 out -> 0임
#     if robot[0] == 0 and belt[0]>=1:
#         robot[0] = 1
#         belt[0] -= 1
#     res += 1
#     if belt.count(0) >= k:
#         break
                
# print(res)