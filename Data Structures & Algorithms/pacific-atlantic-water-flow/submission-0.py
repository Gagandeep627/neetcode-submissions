class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        



        if (not heights):
            return []

        rows, cols = len(heights), len(heights[0])

        pacific = [[False] * cols for _ in range(rows)]

        atlantic = [[False] * cols for _ in range(rows)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r,c, visited):

            visited[r][c] = True


            for (dx, dy) in directions:
                nx, ny = r + dx, c + dy


                if (0<=nx<rows and 0<=ny<cols and not visited[nx][ny] and heights[nx][ny] >= heights[r][c]):
                    dfs(nx, ny, visited)


        # for pacific -->
        # for top corner-->
        for c in range(cols):
            dfs(0, c, pacific)

        # for top-left corner-->
        for r in range(rows):
            dfs(r, 0, pacific)


        
        # for atlantic -->
        # for top-right corner-->
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        # for bottom - corner-->
        for c in range(cols):
            dfs(rows-1, c, atlantic)



        
        # evaluate for matched results 
        # from the both pacific, atlantic visited cells
        result = []
        for r in range(rows):
            for c in range(cols):
                if ((pacific[r][c]) and (atlantic[r][c])):
                    result.append([r,c])

        
        return result
        
