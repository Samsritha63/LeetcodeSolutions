class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        GreaterOrLess = [True]*(len(nums)-1)
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                GreaterOrLess[i] = False
            if nums[i] == nums[i+1]:
                return False
                break
        count = 0
        for j in range(len(GreaterOrLess)-1):
            if GreaterOrLess[j]!=GreaterOrLess[j+1]:
                count+=1
        if count == 2 and GreaterOrLess[i]==True:
            return True
        return False

        