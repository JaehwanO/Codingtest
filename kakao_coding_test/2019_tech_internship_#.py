import re
from itertools import permutations

def solution(user_id, banned_id):
    n = len(banned_id)
    banned_id = [i.replace("*",".") for i in banned_id]
    ans = []
    for i in permutations(user_id,n):
        lst = list(i)
        flag = True
        for j in range(n):
            # print(re.match(banned_id[j],lst[j]))
            if re.match(banned_id[j],lst[j]) and len(banned_id[j]) == len(lst[j]):
                continue
            else:
                flag = False
                break
        if flag:
            if sorted(lst) not in ans:
                ans.append(sorted(lst))
    return len(ans)
    
