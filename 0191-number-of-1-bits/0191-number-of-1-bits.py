class Solution:
    def hammingWeight(self, n: int) -> int:
        summ=bin(n).replace("0b", "")
        res=0
        for i in summ:
            res+=int(i)
        return res 
        
        