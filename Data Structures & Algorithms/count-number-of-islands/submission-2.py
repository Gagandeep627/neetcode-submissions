class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # calculate total rows , total cols-->
        rows, cols = len(grid), len(grid[0])

        # topic : recursion -- brute -- force (approach)-->


        def dfs(r,c):
            # check for row and colns are out of bounds -->
            # check grid(r,c) is 0 to return the out of bound (r,c) for the functions-->
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0"):
                return

            # mark cell grid(r,c) --> "0"
            grid[r][c] = "0"


            # check for all possible positions for the
            # island to hold for the questions to be possible-->
            check_one = (
                
                dfs(r+1,c) or #down
                dfs(r-1,c) or #up
                dfs(r,c+1) or #right
                dfs(r,c-1) #left

            )

            # call check_one functions-->
            return check_one

        count = 0
        # go for every rows-->
        for r in range(rows):
            # go for c : all (columns)-->
            for c in range(cols):
                if (grid[r][c] == "1"): #check for grid(r,c) == 1 containing 1 or not?
                # count += 1, Q).dfs(r, c)-->
                    count += 1
                    dfs(r,c)


        # count : total no. of islands possible so far.. : return count-->
        #Time Complexity : O(m×n), Space Complexity : O(m×n)
        return count