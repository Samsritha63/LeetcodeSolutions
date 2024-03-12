class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1Set=set(nums1)

        nums2Set=set(nums2)

        nums1=list(nums1Set)

        nums2=list(nums2Set)

        unique=[]

        if len(nums1)<len(nums2):

            for i in range(len(nums1)):

                if nums1[i] in nums2:

                    unique.append(nums1[i])

        else:

            for i in range(len(nums2)):

                if nums2[i] in nums1:

                    unique.append(nums2[i])

        return unique

        