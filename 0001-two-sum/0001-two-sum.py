class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if (target - nums[i]) in nums and nums.index(target-nums[i])!=i:
                res.append(i)
                res.append(nums.index(target-nums[i]))
                break
        return res