class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        currentSum=0
        while left <=right:
            currentSum=numbers[left]+numbers[right]
            if currentSum==target:
                return [left+1,right+1]
            elif currentSum>target:
                right-=1
            else:
                left+=1
                