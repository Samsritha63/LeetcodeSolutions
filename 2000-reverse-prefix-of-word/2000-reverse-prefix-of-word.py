class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if ch==word[i]:
                pivot=i
                splitted_words=word.split(ch, 1)
                return (ch+''.join(reversed(splitted_words[0]))+splitted_words[1])
        return word
        
            
        