class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        sol=[]
        for i in range(len(nums)):
            if nums[i]<target:
                continue
            if nums[i]==target:
                sol.append(i)
            if nums[i]>target:
                break
        return sol