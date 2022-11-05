from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    for k in course:
        tmp_list = []
        for i in orders:
            for j in combinations(i,k):
                tmp = ''.join(sorted(j))
                tmp_list.append(tmp)
                
        candidate = Counter(tmp_list).most_common()
        ans += [k for k,v in candidate if v > 1 and v == candidate[0][1]]
    return sorted(ans)