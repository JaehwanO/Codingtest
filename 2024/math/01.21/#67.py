class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        ans = []
        tmp = 0 

        while i>=0 or j>=0 or tmp:
            if i >= 0:
                tmp += int(a[i])
                i -= 1
            if j >= 0:
                tmp += int(b[j])
                j -= 1
            ans.append(str(tmp%2))
            tmp //= 2
        
        return ''.join(reversed(ans))
