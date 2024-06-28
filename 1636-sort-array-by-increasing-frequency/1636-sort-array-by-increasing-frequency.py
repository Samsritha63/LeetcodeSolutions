from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(sorted(nums)).most_common()[::-1]
        res = []
        for v, c in counts :
            res.extend([v for i in range(c)])
        return res