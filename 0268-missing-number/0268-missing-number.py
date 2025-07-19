class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1=sum(nums)
        sum2=int((len(nums)*(len(nums)+1))/2)
        return sum2-sum1
        
        