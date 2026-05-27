class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        # topic : recursive ++ brute force solutions (DFS Solutions) -->


        rows, cols = len(matrix), len(matrix[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c,prev):

            if (r<0 or c<0 or r>=rows or c>=cols):
                return 0

            if (matrix[r][c] <= prev):
                return 0


            longest = 0

            for (dr, dc) in directions:
                longest = max(longest, dfs(r + dr,c + dc, matrix[r][c]))


            return 1 + longest



        ans, prev = 0, -1
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r,c,prev))


        

        return ans
                



        