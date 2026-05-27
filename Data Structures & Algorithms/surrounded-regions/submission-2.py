class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # base case 1:
        if not board or not board[0]:
            return []

        # bae case 2:
        rows, cols = len(board), len(board[0])

        def dfs(r,c):

            # check for 1). out bounds 2).board(r,c) != "O" is equal to X 
            # or oput calculated Safe member --> return simply to the functions-->
            if  ((0>r or r>=rows) or (0>c or c>=cols)) or ((board[r][c] != "O")):
                    return

            # else : board(r, c) -- >"O" 
            # mark board(r,c) --> "S"
            board[r][c] = "S"

            

            dfs(r+1,c)#down
            dfs(r-1,c)#up
            dfs(r,c+1)#right
            dfs(r,c-1)#left

            
        # Q).check for all the members 
        # for all the corner columns 
        # to check if the board(r, c) == "O"
        # if yes then run the dfs(row : r, colmns : c) --> to mark --> 
        # board(r, c) --> mark it S if its board(r,c) -- S

                

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


        # for each and every r,c check for if O is there in the 
        # board(r,c) -- > O  to --> X
        # and if its is S then change it to --> O 
        # return board : our final result ans-->
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O"):
                    board[r][c] = "X"
                elif (board[r][c] == "S"):
                    board[r][c] = "O"


        # ⏳ TIME COMPLEXITY : O(m × n) , 🧠 SPACE COMPLEXITY : O(m × n) Worst Case


        # return board




        



        