n,l,k = map(int,input().split())
task = []
score_0=0
score_100=0
score_140=0

for i in range(n):
    task.append(list(map(int,input().split())))

for i in range(n):
    if task[i][1]<=l: #어려운 버전보다 역량이 높다면
        score_140+=1
    elif task[i][0]<=l and l < task[i][1]:
        #어려운 버전보다 작고 쉬운버전보다 역량이 높다면
        score_100+=1
    else:#둘보다 작으면
        score_0+=1

#k숫자에서 최대한 2를 많이 뽑고, 나머지를 1을 뽑는게좋음
if score_140-k>=0:
    print(k*140)
elif score_140-k<0 and score_140+ score_100-k>=0:
    print(140*score_140+100*(k-score_140))
elif score_140+score_100-k<0:
    print(140*score_140+100*score_100)

# n,l,k = map(int, input().split())
# score = 0
# easy=[]
# hard=[]
# for _ in range(n):
#     a,b = map(int,input().split())
#     easy.append(a)
#     hard.append(b)
#     # if b<=l:
#     #     score += 140
#     #     k-=1
#     # elif a <=l and b>=l:
#     #     score +=100
#     #     k-=1
#     # elif k ==0:
#     #     print(score)
#     # # elif _==n-1:
#     # #     print(score)
# for i in range (len(hard)):
#     if k!=0 and hard[i] <= l:
#         score += 140
#         k -= 1
# if len(easy) > 0:        
#     for i in range (len(easy)):
#         if k!=0 and easy[i] <= l:
#             score += 100
#             k -= 1
# print(score)
# 