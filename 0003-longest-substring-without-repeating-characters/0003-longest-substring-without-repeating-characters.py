class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        sett = set()
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
            sett.add(s[right])
            maxLen = max(maxLen, right-left+1)
        return maxLen