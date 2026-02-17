class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (len(nums)*(len(nums)+1))/2
        actual = sum(nums)
        return int(total - actual)