class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = 0
        A_set=set()
        B_set=set()
        res=[]
        for i in range(len(A)):
            if A[i] in B_set:
                common+=1
            if B[i] in A_set:
                common+=1
            if A[i]==B[i]:
                common+=1
            A_set.add(A[i])
            B_set.add(B[i])
            res.append(common)
        return res