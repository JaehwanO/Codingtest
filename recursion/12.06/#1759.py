def back(cnt,idx):
    if cnt == L:
        vo, co = 0,0
        for i in range(L):
            if ans[i] in consonant:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(ans))
        return
        
    for i in range(idx,C):
        ans.append(words[i])
        back(cnt+1,idx+1)
        ans.pop()



L,C = map(int,input().split())
words = sorted(list(map(str,input().split())))
consonant = ['a', 'e', 'i', 'o', 'u']
ans = []
back(0,0)
