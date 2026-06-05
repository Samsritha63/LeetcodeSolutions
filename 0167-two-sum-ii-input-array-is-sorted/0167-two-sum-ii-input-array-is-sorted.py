class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        currSum = float('inf')
        while l < n:
            currSum = (numbers[l] + numbers[r])
            if currSum == target:
                return [l+1,r+1]
            elif currSum > target:
                r-=1
            else:
                l+=1