class Solution:
    def solve(self, board: List[List[str]]) -> None:


        if not board or not board[0]:
            return []

        rows, cols = len(board), len(board[0])

        def dfs(r,c):


            if  ((0>r or r>=rows) or (0>c or c>=cols)) or ((board[r][c] != "O")):
                    return

            board[r][c] = "S"

            

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            

                

        # top corner-->
        for c in range(cols):
            if (board[0][c] == "O"):
                dfs(0, c)

        # bottom corner-->
        for c in range(cols):
            if (board[rows-1][c] == "O"):
                dfs(rows-1, c)

        
        # left corner-->
        for r in range(rows):
            if (board[r][0] == "O"):
                dfs(r, 0)

        # right corner-->
        for r in range(rows):
            if (board[r][cols-1] == "O"):
                dfs(r, cols-1)


        

        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O"):
                    board[r][c] = "X"
                elif (board[r][c] == "S"):
                    board[r][c] = "O"


        
        # return board




        



        