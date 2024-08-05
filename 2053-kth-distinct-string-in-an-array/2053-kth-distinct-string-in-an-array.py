class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c=Counter(arr)
        sol=[]
        for i in range(len(arr)):
            if c[arr[i]]==1:
                sol.append(arr[i])
        if len(sol)>=k:
            return sol[k-1]
        else:
            return ""