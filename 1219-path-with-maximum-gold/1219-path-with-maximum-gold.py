class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, i, j, gold):
            mx = gold
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0<=x<r and 0<=y<c and grid[x][y]:
                    tmp, grid[x][y] = grid[x][y], 0
                    mx = max(mx, dfs(grid, r, c, x, y, gold+tmp))
                    grid[x][y] = tmp
            return mx
        
        r, c, mx = len(grid), len(grid[0]), 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    tmp, grid[i][j] = grid[i][j], 0
                    mx = max(mx, dfs(grid, r, c, i, j, tmp))
                    grid[i][j] = tmp
        return mx