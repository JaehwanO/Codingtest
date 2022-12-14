import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = re.sub('[^a-z0-9]','',s)
        return new_s == new_s[::-1]