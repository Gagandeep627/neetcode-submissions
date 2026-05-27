class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # topic : backtracking approach-->

        result = []
        cols = set()
        diag1 = set()
        diag2 = set()


        board = [["."] * n for _ in range(n)]


        
        def dfs(row):


            if (row == n):
                ans0 = ["".join(r) for r in board]
                result.append(ans0)
                
                return



            for col in range(n):


                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue

                
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)


                dfs(row+1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)


        initial_row = 0
        dfs(initial_row)
        return result    

























        