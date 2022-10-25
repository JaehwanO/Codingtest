from itertools import combinations #조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

#조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N//2)):
    possible_team.append(team)

min_stat_gap = 10000 #갭이 가장 작은 값을 찾기 위하여
for i in range(len(possible_team)//2):
    #A 팀
    team = possible_team[i]
    stat_A = 0 #A팀 능력치
    for j in range(N//2):
        member = team[j] #멤버
        for k in team:
            stat_A += S[member][k] #멤버와 함께할 경우의 능력치들
            
    #A를 제외한 나머지 팀
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]
            
    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))
    
print(min_stat_gap)

# 시간초과
# from itertools import permutations
# import sys
# n = int(input())
# l = [i for i in range(1,n+1)]
# per = permutations(l,n//2)
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))


# start_link = []
# ans = sys.maxsize
# for i in per:
#     start = 0
#     link = 0
#     a = list(i)
#     b = [x for x in l if x not in a]

#     for j in range(len(a)-1):
#         for k in range(j+1,len(a)):
#             start += graph[a[j]-1][a[k]-1] + graph[a[k]-1][a[j]-1]

#     for j in range(len(a)-1):
#         for k in range(j+1,len(a)):
#             link += graph[b[j]-1][b[k]-1] + graph[b[k]-1][b[j]-1]
#     tmp = start - link
#     if tmp >= 0:
#         ans = min(ans,start-link)  
# print(ans)

