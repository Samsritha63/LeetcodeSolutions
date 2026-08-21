class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            for k in range(j+1, len(nums2)):
                if nums2[k] > nums1[i]:
                    ans.append(nums2[k])
                    break
            else:
                ans.append(-1)
        return ans
        