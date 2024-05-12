class Solution(object):
    def largestLocal(self, grid):
        res=[]

        for i in range(1,len(grid)-1):
            tmp=[]
            for  j in range(1,len(grid[i])-1):
                localMax=max(grid[i][j],grid[i][j+1],grid[i][j-1],grid[i-1][j],grid[i+1][j],grid[i-1][j-1],grid[i-1][j+1],grid[i+1][j-1],grid[i+1][j+1])
                tmp.append(localMax)
            res.append(tmp)

        return res