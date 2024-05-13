class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        res=n*(2**(m-1))
        for c in range(1,m):
            cnt =0
            for r in range(n):
                if grid[r][c]!=grid[r][0]:
                    cnt+=1
            cnt=max(cnt,n-cnt)
            res+=cnt*(2**(m-c-1))
        return res
        