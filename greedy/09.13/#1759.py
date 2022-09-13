import sys
from itertools import combinations
input = sys.stdin.readline
n,c = map(int,input().split())
alp = list(map(str,input().split()))
alp.sort()
mo = set(['a','e','i','o','u'])

def code():
    result = []
    for c in list(combinations(alp,n)):
        vowel_cnt = consonant_cnt = 0
        for char in c:
            if char in mo:
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        if vowel_cnt >0 and consonant_cnt > 1:
            result.append(''.join(c))
    return result

for p in code():
    print(p)