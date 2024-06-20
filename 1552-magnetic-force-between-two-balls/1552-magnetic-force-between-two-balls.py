class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position=sorted(position)
        n=len(position)
        left=1
        right=position[-1]-position[0]
        def count_balls(d):
            n_balls=1
            cur=position[0]
            for i in range(1,n):
                if position[i]-cur>=d:
                    n_balls+=1
                    cur=position[i]
            return n_balls
        while left<=right:
            mid=(left+right)//2
            if count_balls(mid)>=m:
                left=mid+1
            else:
                right=mid-1
        return right