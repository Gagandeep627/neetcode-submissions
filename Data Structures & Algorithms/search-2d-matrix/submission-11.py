class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # Topic : Binary Search...
        # m * n matrix -->


        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])

        #start from 0 th element -->
        start = 0

        #traversal over m * n - 1 elements -->
        end = (m * n) - 1

        # mid = (start + end) // 2


        # scans through all of the elements as all subarrays are also sorted merge them into a one aray-->
        while (start <= end):
            #calc --> mid.. 
            mid = (start + end) // 2
            #for a 2 D array remember the formula to evaluate the row th && column 
            #th for a 2 D array..
            # row = integer value of (mid // n)
            row = mid // n
            # column = remainder of (mid % n)
            column = mid % n

            #normal binary search enabled -- code stated..
            if (matrix[row][column] == target):
                return True
            elif (matrix[row][column] < target):
                start = mid + 1
            else:
                end = mid - 1

        # time_complexity binary search : O(log(elements covered uptill (m * n - 1))
        # O(log(m * n)) -->
        # space_complexity : O(1) -->
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

            
        