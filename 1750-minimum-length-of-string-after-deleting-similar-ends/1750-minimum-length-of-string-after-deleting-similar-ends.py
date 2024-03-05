class Solution:
    def minimumLength(self, s: str) -> int:
        # create 2 pointers
        left=0
        right=len(s)-1
        # only enter if the ends are same
        while (left<right) and s[left]==s[right]:
            # pick the common character
            ch=s[left]
            # get prefix with same characters
            while (left<=right) and s[left] == ch:
                left+=1
            # get suffix with same characters
            while (right>=left) and s[right] == ch:
                right-=1
        # make sure that left and right doesnt intersect, if they do, nothing works
        if left > right:
            return 0
        # return the result
        else:
            return right-left+1
            
                

        