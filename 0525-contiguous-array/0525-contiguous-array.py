class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmapp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in hashmapp:
                max_len = max(max_len, i - hashmapp[sum_val])
            else:
                hashmapp[sum_val] = i
        return max_len