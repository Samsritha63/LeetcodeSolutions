class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sol=[]
        for i in range(n):
            cur_sum=0
            for j in range(i,n):
                cur_sum+=nums[j]
                sol.append(cur_sum)
        sol=sorted(sol)
        return sum(sol[left-1:right])%(10**9 + 7)
        