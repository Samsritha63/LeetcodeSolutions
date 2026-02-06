class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        ans = 0
        j = 0
        for i in range(n):
            while j + 1 < n and nums[i] * k >= nums[j + 1]:
                j += 1
            ans = max(ans, j - i + 1)

        return n - ans