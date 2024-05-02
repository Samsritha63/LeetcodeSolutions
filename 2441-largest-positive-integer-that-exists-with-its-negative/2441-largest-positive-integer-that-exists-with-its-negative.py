class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_num = -1
        nums_set = set(nums)
        for i in nums:
            if i > 0:
                if i > max_num and -i in nums_set:
                    max_num = i
        return max_num