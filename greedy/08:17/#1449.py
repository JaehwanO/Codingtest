N,L = map(int,input().split())
leak=list(map(int,input().split()))
leak.sort()
#0.5만큼의 간격 ? = 각 센치미터 단위의 중앙에 위치하여한다는 뜻
tape=1
dist=0#구멍간의 거리
for i in range(1,N):
    dist +=abs(leak[i]-leak[i-1]) 
    if L > dist:
        continue
    else:
        tape+=1
        dist=0
print(tape)