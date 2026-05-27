class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # Topic : Binary Search...


        if not matrix or not matrix[0]:
            return False
    
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n      # Row index
            col = mid % n       # Column index
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

            
        