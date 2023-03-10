data = []

for _ in range(5) :
  data.append(input())

flag = 0
for i in range(len(data)) :
  if 'FBI' in data[i] :
    print(i+1, end=' ')
    flag = 1

if flag == 0 :
  print('HE GOT AWAY!')