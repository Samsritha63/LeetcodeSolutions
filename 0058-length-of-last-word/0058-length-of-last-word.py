class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array_of_words=s.strip().split()
        if not array_of_words:
            return 0
        return len(array_of_words[-1])
        