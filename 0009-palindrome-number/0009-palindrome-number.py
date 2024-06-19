class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        b=str(a[::-1])
        # print(a,b)
        return a==b 