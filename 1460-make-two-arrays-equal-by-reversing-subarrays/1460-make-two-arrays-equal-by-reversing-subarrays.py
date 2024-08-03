from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c,s=Counter(target),Counter(arr)
        return c==s
        