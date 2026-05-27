class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # Topic : Binary Search...
        # m * n matrix -->


        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        start = 0

        end = (m * n) - 1

        # mid = (start + end) // 2



        while (start <= end):
            mid = (start + end) // 2
            row = mid // n
            column = mid % n

            if (matrix[row][column] == target):
                return True
            elif (matrix[row][column] < target):
                start = mid + 1
            else:
                end = mid - 1


        return False

                

            





























        # if not matrix or not matrix[0]:
        #     return False
    
        # m, n = len(matrix), len(matrix[0])
        # left, right = 0, m * n - 1

        # while left <= right:
        #     mid = (left + right) // 2
        #     row = mid // n      # Row index
        #     col = mid % n       # Column index
            
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return False

            
        