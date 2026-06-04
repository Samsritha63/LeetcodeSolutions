from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        res = []
        for i in range(len(s)-len(p)+1):
            if s[i] in p:
                subString = s[i:i+len(p)]
                sub_counter = Counter(subString)
                if p_counter == sub_counter:
                    res.append(i)
        return res