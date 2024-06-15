class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        projects=[(capital[i],profits[i]) for i in range(n)]
        projects.sort()
        sol=[]
        i=0
        for p in range(k):
            while i<n and projects[i][0]<=w:
                heapq.heappush(sol,-projects[i][1])
                i+=1
            if not sol:
                break
            w-=heapq.heappop(sol)
        return w