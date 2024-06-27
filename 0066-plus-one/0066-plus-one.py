class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=""
        sol=[]
        for i in digits:
            res+=str(i)
        res=int(res)
        res+=1
        res=str(res)
        for i in res:
            sol.append(int(i))
        return sol