from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        window = Counter()
        res = []
        k = len(p)
        for i in range(len(s)):
            window[s[i]]+=1
            if i >= k:
                left_char = s[i - k]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

            if window == p_count:
                res.append(i - k + 1)

        return res