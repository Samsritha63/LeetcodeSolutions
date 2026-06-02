class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        currSum = 0
        minLen = float('inf')
        while r < n:
            currSum += nums[r]
            r += 1
            while currSum >= target:
                minLen = min(minLen, r - l)
                currSum -= nums[l]
                l +=1
        return 0 if minLen == float('inf') else minLen