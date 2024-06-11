class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        # Traverse through the relative order array
        for value in arr2:
            # Traverse through the target array
            for j in range(len(arr1)):
                # Element in target array matches with relative order element
                if arr1[j] == value:
                    # Add it to the result array
                    result.append(arr1[j])
                    # Mark the element in target array as visited
                    arr1[j] = -1
        # Sort the remaining elements in the target array
        arr1.sort()
        # Add the remaining elements to the result array
        for value in arr1:
            if value != -1:
                result.append(value)
        return result