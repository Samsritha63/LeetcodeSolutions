from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        l, r = 0, 0
        k = len(p)
        window = Counter()
        res = []
        for i in range(len(s)):
            window[s[i]]+=1
            if i >= k:
                left = s[i-k]
                window[left]-=1

                if window[left] == 0:
                    del window[left]
            if p_count == window:
                res.append(i-k+1)
        return res