class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        maxFreq = 0
        maxLen = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1

            maxFreq = max(maxFreq, count[idx])

            while (right - left + 1) - maxFreq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen