class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            curr = target - nums[i]
            if curr in nums and i != nums.index(curr):
                res.append(i)
                res.append(nums.index(curr))
                return res