n,m = map(int,input().split())
book = list(map(int, input().split()))

plus = []
minus = []
count = []

# //양수와 음수부분을 나눠주되, 음수부분은 절대값을 씌워줌
for i in book:
    if i>0:
        plus.append(i)
    else:
        minus.append(abs(i))

# //내림차순으로 정렬
plus.sort(reverse=True)
minus.sort(reverse=True)

# //m*i 번째 리스트를 count 리스트에 추가. if문을 통해 남는 리스트 중 가장 큰 값을 count에 넣어준다.
for i in range(len(plus)//m):
    count.append(plus[i*m])
if len(plus)%m>0:
    count.append(plus[(len(plus)//m)*m])

for i in range(len(minus)//m):
    count.append(minus[i*m])
if len(minus)%m>0:
    count.append(minus[(len(minus)//m)*m])

count.sort()

# //마지막에는 제자리로 돌아올 필요가 없기 때문에 최대값만 그냥 result에 넣고 나머지는 2를 곱해 더한다.
result = count.pop()
result += 2*sum(count)

print(result)