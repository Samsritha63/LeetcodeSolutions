class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i=0
        while i+2<len(arr):
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
            i+=1
        return False      