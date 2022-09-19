n = int(input())

s = [0, 1, 3]
for i in range(3, n+1):
  s.append(s[i - 2] + s[i - 1] + s[i-2])
  
print(s[n] % 10007)