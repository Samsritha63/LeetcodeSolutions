class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums=sorted(nums)
        moves=0
        maxx=0
        for num in nums:
            maxx=max(num,maxx)
            moves+=maxx-num
            maxx+=1
        return moves   