class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = str(bin(n))[2:]
        if "11" in n:
            return False
        elif "00" in n:
            return False
        else:
            return True