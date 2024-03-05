class Solution:
    def minimumLength(self, s: str) -> int:
        left=0
        right=len(s)-1
        while (left<right) and s[left]==s[right]:
            ch=s[left]
            while (left<=right) and s[left] == ch:
                left+=1
            while (right>=left) and s[right] == ch:
                right-=1
        if left > right:
            return 0
        else:
            return right-left+1
            
                

        