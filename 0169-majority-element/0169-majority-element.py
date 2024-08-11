class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i in range(len(nums)):
            if c[nums[i]]>(len(nums)//2):
                return nums[i]      