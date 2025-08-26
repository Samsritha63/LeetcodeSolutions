class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag=1
        max_area=1
        for arr in dimensions:
            curr_diag=((arr[0]**2 + arr[1]**2)**(0.5))
            curr_area=arr[0]* arr[1]
            if max_diag<curr_diag:
                max_area = curr_area
                max_diag=curr_diag
            elif max_diag==curr_diag:
                max_area=max(max_area, curr_area)
        return max_area