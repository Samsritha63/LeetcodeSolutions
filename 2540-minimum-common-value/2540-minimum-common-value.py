from collections import Counter
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        arr=[]
        if len(nums1) > len(nums2):
            c1=Counter(nums1)

            nums2=sorted(nums2)
            for i in range(len(nums2)):
                if nums2[i] in c1:
                    arr.append(nums2[i])
                    break

        else:
            c2=Counter(nums2)
            nums1=sorted(nums1)
            for i in range(len(nums1)):
                if nums1[i] in c2:
                    arr.append(nums1[i])
                    break
        if len(arr)>0:
            return arr[0]
        else:
            return -1