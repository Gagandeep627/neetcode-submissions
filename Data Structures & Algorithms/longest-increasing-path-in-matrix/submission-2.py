class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        # topic : recursive ++ memoizations version--> 
        rows, cols = len(matrix), len(matrix[0])

        # directiions : up, down, left, right
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        # dp[r][c] will store increasing path starting from (r,c) -->
        dp = [[-1] * cols for _ in range(rows)] #Memo table + recursion stack in worst case.
        

        # The longest path starting from (r,c) is always the same,
        def dfs(r,c):
            # if already computed, return memoized value-->
            if (dp[r][c] != -1):
                return dp[r][c]

            longest = 1 # at least the cell itself


            # Each cell is computed once, and each checks 4 neighbors.
            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc

                # check boundaruies + strictly increasinbg conditions
                if (0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[r][c]):
                    longest = max(longest, 1 + dfs(nr,nc))


            dp[r][c] = longest

            return longest



        ans = 0 
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r,c))

        return ans



#         ✔ Time = O(m · n)

# Each cell is computed once, and each checks 4 neighbors.

# ✔ Space = O(m · n)

# Memo table + recursion stack in worst case.
                




























        # topic : recursive ++ brute force solutions (DFS Solutions) -->


        # rows, cols = len(matrix), len(matrix[0])

        # directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # def dfs(r,c,prev):
        # if out of bounds or not strictly increasing -> stop:
        #     if (r<0 or c<0 or r>=rows or c>=cols):
        #         return 0

        #     if (matrix[r][c] <= prev):
        #         return 0


        #     longest = 0

        #     for (dr, dc) in directions:
        #         longest = max(longest, dfs(r + dr,c + dc, matrix[r][c]))


        #     return 1 + longest #count current cell


        # start DFS from every cell.
        # ans, prev = 0, -1
        # for r in range(rows):
        #     for c in range(cols):
        #         ans = max(ans, dfs(r,c,prev))


        

        # return ans



#         | Approach                    | Time      | Space | Notes               |
# | --------------------------- | --------- | ----- | ------------------- |
# | **Brute Recursive**         | `4^(m*n)` | `m*n` | Very slow, no reuse |
# | **Recursive + Memoization** | `m*n`     | `m*n` | Best + easiest      |

                



        