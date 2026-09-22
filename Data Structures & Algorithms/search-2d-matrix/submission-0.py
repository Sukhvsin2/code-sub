class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # first index 0 and last index is m * n - 1
        l, r = 0, rows*cols-1


        while l <= r:
            mid = (l + r) // 2 # found the mid

            val = matrix[mid // cols][mid % cols] # val at mid index

            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True

        return False