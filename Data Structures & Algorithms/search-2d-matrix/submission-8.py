class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # Topic : Binary Search...


        row = 0
        found = False
        n = len(matrix[0])
        m = len(matrix)

        # if (m == 1 and n == 1):
        #     if (matrix[0][0] == target):
        #         return True
        #     else:
        #         return False
        if (m == 1):
            if (target in matrix[0]):
                return True
            else:
                return False

        #time : O(0 ..... row where target is prsent --> i)
        while (row <= m):
            if (row == m):
                return False

            if (matrix[row][-1] >= target):
                break
            row += 1

        # while (matrix[row][-1] < target):
        #     row += 1


        # if (row >= m):
        #     return False
        
        nums = matrix[row]

        # print(nums)


        start , end = 0, n - 1

        #time : O(Log(n))
        while (start <= end):

            mid = (start + end) // 2

            if (nums[mid] == target):
                found = True
                return found
            elif (nums[mid] > target):
                end = mid - 1
            else:
                start = mid + 1

            #time_Complexity : O(0 ..... row where target is prsent --> i) + O(Log(n)) --> O(Log(n))
        return found 

            
        