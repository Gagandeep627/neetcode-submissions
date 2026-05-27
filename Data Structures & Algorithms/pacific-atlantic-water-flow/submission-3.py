class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # topic : Matrix DFS


        if (not heights):
            return []

        rows, cols = len(heights), len(heights[0])

        # make a visited(pacific, atlantic) --> array for 
        # to check for which (row : r, column : c) are being visited or not..

        pacific = [[False] * cols for _ in range(rows)]

        atlantic = [[False] * cols for _ in range(rows)]

        # make of with the directions as like stated..
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r,c, visited):
            # start of recurse functions..
            #  mark visited(r)(c) = True
            visited[r][c] = True

            # move to each of the directions as stated
            # up, down, left, right
            #calculate (nx, ny) for each subset directions listed so far..
            for (dx, dy) in directions:
                nx, ny = r + dx, c + dy

                # check for the bound conditions --> 
                if (0<=nx<rows and 0<=ny<cols):
                    # if the cell is not visited && 
                    # && heights(nx)(ny) > current_heigh(r,c) -->
                    #start with the dfs function again to find  out with next possible 
                    # cell(r, c) so far where heights(nr, nc) > curr_height(r,c)
                    if (not visited[nx][ny] and heights[nx][ny] >= heights[r][c]):
                        dfs(nx, ny, visited)


        # for pacific (top and top-left corner dfs() functions-->
        # have been runned to check for the all visited (r, c) for the 
        # dfs() functions for the pacific_matrix's(r,c-->
        # for top corner-->
        for c in range(cols):
            dfs(0, c, pacific)

        # for top-left corner-->
        for r in range(rows):
            dfs(r, 0, pacific)



        # for atlantic (bottom and botoom right) and top-left corner dfs() functions-->
        # have been runned to check for the all visited (r, c) for the 
        # dfs() functions for the pacific_matrix's(r,c-->

        
        # for atlantic -->
        # for top-right corner-->
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        # for bottom - corner-->
        for c in range(cols):
            dfs(rows-1, c, atlantic)



        
        # evaluate for matched results 
        # from the both pacific, atlantic visited cells
        # for all visited cells for (pacific && atlantic)
        # the cells where the dfs(nr, nc) --> remanded true
        # dfs() fucntions was been able to reach that farthest most cell so far
        # take the intersections of the both matrix
        # corrosponding to pacific(r, c) && atlantic(r,c) == True -->
        # if both are sums to true --> add(r,c) in the result
        # and return the resultant matrix as the answer->



        result = []
        for r in range(rows):
            for c in range(cols):
                if ((pacific[r][c]) and (atlantic[r][c])):
                    result.append([r,c])

        # time : So max ≈ 2 × (m × n) → still O(m × n)
        # SPACE IS O(m × n)

        # ans --> resultant : intersections of true values indexes (r, c)
        # of pacific meets with the atlantic coincidence visited cell-->
        # return : ans; 
        return result
        
