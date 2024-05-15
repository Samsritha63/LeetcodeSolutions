class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n,q = len(grid),deque([])

        if grid[0][0] or grid[n-1][n-1]:
            return 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i,j))
                    grid[i][j]=0
                else:
                    grid[i][j]=-1

        # bfs to find min dist of all cells from thief
        visited = set()
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            for i in range(len(q)):
                x,y = q.popleft()

                if (x,y) in visited:
                    continue
                
                visited.add((x,y))
                for dx,dy in dir:
                    r,c = x+dx,y+dy
                    if 0<=r<n and 0<=c<n and grid[r][c]==-1:
                        grid[r][c] = grid[x][y]+1
                        q.append((r,c))
                
        
        # dijkstra to get max safeness factor
        heap = [(-grid[0][0],0,0)] #dist,x,y
        ans = grid[0][0]
        visited = set()

        while heap:
            dist,x,y = heappop(heap)
            ans = min(ans,-dist)

            if x==n-1 and y==n-1:
                return ans 

            if (x,y) in visited:
                continue

            visited.add((x,y))

            for dx,dy in dir:
                r,c = x+dx,y+dy
                if 0<=r<n and 0<=c<n:
                    heappush(heap,(-grid[r][c],r,c))

        return ans