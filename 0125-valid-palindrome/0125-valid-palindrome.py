class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res+=i.lower()
        mid = len(res)//2
        if len(res)%2==0 and res[:mid] == res[mid:][::-1]:
            return True
        elif len(res)%2!=0 and res[:mid] == res[mid+1:][::-1]:
            return True
        return False