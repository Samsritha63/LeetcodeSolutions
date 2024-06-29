class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1=Counter(s)
        c2=Counter(t)
        return c1==c2
        