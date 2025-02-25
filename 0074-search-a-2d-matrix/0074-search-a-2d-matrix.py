class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n = len(mat)  
        m = len(mat[0]) 


        left, right = 0, n * m - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = mat[mid // m][mid % m]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
            