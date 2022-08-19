s = str(input())
p = str(input())

l =[]

for i in range(len(s)):
    l.append(s[i::])
print(l)
i = 0
while len(p) > 1:
    # if i == len(l):
    #     i = 0
    if l[i] in p:
        new = p.replace(l[i],'')
        p = new
        print(new)
    else:
        i+=1
        
print(new)