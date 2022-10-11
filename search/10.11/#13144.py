n = int(input())
s = list(map(int,input().split()))
ans=0
start,end = 0,0
visit = [False]*100001
while start!=n and end!=n:#시작 지점과 끝나는 지점이 n이면 멈춰줌 
    if not visit[s[end]]:#끝나는 지점이 안 나온 수 라면 앞으로 전진해줌
        visit[s[end]]=True
        end+=1
        ans+=end-start
      
    else:
        while visit[s[end]]:#s[en]이 참인 경우 = 앞에 중복되는 숫자가 이미 나왔다.
            visit[s[start]]=False#앞에 나온 숫자는 이제 안 쓸거므로 False로 바꿔줌
            start+=1#다음 숫자로 이동
    
print(ans)#결과 출력