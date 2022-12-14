import collections, re, List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        count = collections.Counter(words)
        return (count.most_common(1)[0][0])