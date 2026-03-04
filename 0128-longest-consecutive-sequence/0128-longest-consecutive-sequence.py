class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))  # remove duplicates
        longest = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1

        return max(longest, curr) if nums else 0