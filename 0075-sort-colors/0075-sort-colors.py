class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        final = {0:0,1:0,2:0}
        for i in range(len(nums)):
            if nums[i] in final:
                final[nums[i]]+=1
        index=0
        for color in [0,1,2]:
            for j in range(final[color]):
                nums[index]=color
                index+=1
        