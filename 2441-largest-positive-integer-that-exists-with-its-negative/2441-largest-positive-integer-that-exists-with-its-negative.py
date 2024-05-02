class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_num=-1
        nums=sorted(nums)
        
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if (nums[i]*(-1)) in nums:
                max_num=max(max_num,abs(nums[i]))
        return max_num
            
        