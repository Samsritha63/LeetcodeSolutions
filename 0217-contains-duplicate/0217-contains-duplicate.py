class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for i in range(len(nums)):
            if i+1<len(nums):
                if nums[i]==nums[i+1]:
                    return True
        return False
        