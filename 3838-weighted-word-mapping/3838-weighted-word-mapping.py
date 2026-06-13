class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res_weights = []
        final = ""
        curr = 0
        for s in words:
            curr_weight = 0
            for i in s:
                curr = ord(i)
                curr_weight+= weights[curr - 97]
            res_weights.append(curr_weight%26)
        for j in range(len(res_weights)):
            temp = res_weights[j]
            temp = 25 - temp
            letter = chr(temp+97)
            final+=letter
        return final
            
        