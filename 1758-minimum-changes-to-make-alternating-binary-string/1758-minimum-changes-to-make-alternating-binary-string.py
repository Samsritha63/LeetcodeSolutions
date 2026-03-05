class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count0, count1 =0, 0
        for i in range(n):
            if ((i%2)==0 and s[i]!="0") or ((i%2)!=0 and s[i]!="1"):
                    count0+=1
            if ((i%2)==0 and s[i]!="1") or ((i%2)!=0 and s[i]!="0"):
                count1+=1
        return min(count0, count1)