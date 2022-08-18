import sys
n=int(input())
hoe=[]#회의 시작 끝시각,#회의시간

for i in range(n):
    hoe.append(list(map(int,sys.stdin.readline().split())))
    hoe[i].append(hoe[i][1]-hoe[i][0])


hoe.sort(key=lambda x:(x[0],x[2])) #회의시작시간을 기준으로 오름차순 정렬하고 같다면, 회의시간으로 오름차순정렬
#print(hoe)

count=0#회의 수
pre=[[0,0,0]]#이전회의의 종료시간

for i in hoe:
    #print(pre)
    if i[0]>pre[0][0] and i[1]<pre[0][1]:#이번의 순서가 전 회의시간 안에 포함되는 경우 이로 대체
        pre[0]=i
        continue
    if i[0]>=pre[0][1]:
        count+=1
        pre[0]=i

print(count)

# n = int(input())
# l = []
# for _ in range(n):
#     l.append(list(map(int,input().split())))
    
# l = sorted(l, key=lambda x: (x[1],-x[0]))
# # print(l)
# t = 0
# cnt = 0
# t = l[0][1]
# for i in range(n):
#     if l[i][0] >= t:
#         # print(t)
#         t = l[i][1]
#         cnt +=1
# print(cnt+1)