class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):


            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            # mark as visited
            grid[r][c] = 0

            area = 1

            area += dfs(r + 1, c)  # down
            area += dfs(r - 1, c)  # up
            area += dfs(r, c + 1)  # right
            area += dfs(r, c - 1)  # left


            return area



        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_area = dfs(r,c)
                    max_area = max(max_area, curr_area)



        return max_area

