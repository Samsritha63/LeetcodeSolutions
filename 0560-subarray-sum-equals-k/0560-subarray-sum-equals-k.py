class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        counts = 0
        curr = 0
        prefix_sums[0] = 1

        for num in nums:
            curr +=num
            counts += prefix_sums[curr - k]
            prefix_sums[curr] += 1
        return counts
        