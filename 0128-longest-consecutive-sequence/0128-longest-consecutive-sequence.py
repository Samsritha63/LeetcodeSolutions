class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = sorted(set(nums))
        # longest, curr = 1, 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         curr+=1
        #     else:
        #         longest = max(longest,curr)
        #         curr = 1
        # return max(longest, curr) if nums else 0

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length=1
                curr = num
                while curr + 1 in numSet:
                    curr+=1
                    length+=1
                longest = max(longest, length)
        return longest