class Solution:
    def binaryGap(self, n: int) -> int:
        temp = bin(n)
        temp = temp[2:]
        print(temp)
        res = []
        for index, char in enumerate(temp):
            if char == "1":
                res.append(index)
        if len(res)==1 or len(res) == 0:
            return 0
        res = sorted(res)
        gap = 0
        for i in range(len(res)-1):
            if res[i+1]-res[i] > gap:
                gap = max(gap,(res[i+1]-res[i]))
        return gap