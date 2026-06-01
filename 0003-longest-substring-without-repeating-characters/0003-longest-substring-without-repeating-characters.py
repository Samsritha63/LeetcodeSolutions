class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,maxLen = 0, 0
        seen_set = set()
        for right in range(len(s)):
            while s[right] in seen_set:
                seen_set.remove(s[left])
                left+=1
            seen_set.add(s[right])
            maxLen = max(maxLen, right - left +1)
        return maxLen
        