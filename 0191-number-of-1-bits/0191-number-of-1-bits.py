class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        str1 = str(binary)
        count = 0
        for i in str1:
            if i == "1":
                count+=1
        return count
        