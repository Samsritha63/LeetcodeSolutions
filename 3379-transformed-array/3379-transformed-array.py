class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                index = (i+nums[i]) % len(nums)
                res[i] = nums[index]
        return res