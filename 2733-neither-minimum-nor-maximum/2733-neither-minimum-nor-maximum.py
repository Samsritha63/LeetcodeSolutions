class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        for i in range(len(nums)):
            if nums[i]!=mini and nums[i]!=maxi:
                return nums[i]
        return -1
        