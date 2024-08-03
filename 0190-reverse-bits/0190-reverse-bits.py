class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert the number to a 32-bit binary string
        num = format(n, '032b')
        
        # Reverse the binary string
        num = num[::-1]
        
        # Convert the reversed binary string back to an integer
        return int(num, 2)
