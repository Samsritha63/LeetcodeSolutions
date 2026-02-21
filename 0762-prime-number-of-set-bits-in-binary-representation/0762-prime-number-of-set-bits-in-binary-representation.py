class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for i in range(left, right+1):
            temp = bin(i)
            temp = temp[2:]
            count = 0
            for j in temp:
                if j == "1":
                    count+=1
            if count in primes:
                res+=1
        return res
        