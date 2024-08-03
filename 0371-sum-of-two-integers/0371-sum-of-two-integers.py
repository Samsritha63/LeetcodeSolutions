class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        # Integer max
        MAX = 0x7FFFFFFF

        while b != 0:
            # ^ gets different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
        return a if a <= MAX else ~(a ^ MASK)

            
        