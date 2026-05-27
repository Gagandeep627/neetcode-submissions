class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # topic : backtracking approach-->

        # Space is used in three places:
         # This list will store ALL valid solutions
        result = []
        # 3️⃣ Sets (cols, diag1, diag2) : At most n elements each : → O(n) 
          # These sets help us check if a position
        cols = set()
        diag1 = set()
        diag2 = set()

         # Create an empty chessboard
    # '.' means empty cell
        board = [["."] * n for _ in range(n)] #n × n board → O(n²)


        # Depth = n (one recursive call per row) → O(n)
        # backtracking : 
        # each row tells which row we are currently filling:
        def dfs(row):

            # base case: row = n ( it means we have placed)
            # queens successfully in all rows
            if (row == n):
                ans0 = ["".join(r) for r in board]
                result.append(ans0)
                
                return


            #loop 1: try placing a queen in every column
            #of the current row:

            for col in range(n):
                
                #safety check:
                #if column or diagonals are already used,
                #we cannot place a queen here..

                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue


                #place queen (choose step):-
                # We place one queen per row
                # For each row, we try different columns
                # Once a column is used, it cannot be reused
                # So effectively, we are trying permutations of columns
                board[row][col] = "Q" #place queen on board
                cols.add(col) #mark column as occupied 
                diag1.add(row-col) #mark left diagonal 
                diag2.add(row+col) #mark right diagonal

                #recursive call:
                #move to next row:
                dfs(row+1)

                #BACTRACK (undo step):
                #remove the queen and free the sets
                board[row][col] = "." #
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)


        # 🔹 What actually happens?

        # ✅ Time Complexity = O(n!)
        # Row 0 → up to n choices
        # Row 1 → up to n−1 choices
        # Row 2 → up to n−2 choices
        # Total ≈ n × (n−1) × (n−2) × ... = n!
        # Diagonal checks are O(1) using sets, so they don’t change the order.
        # ✅ Total Space Complexity : The dominant term is the board: O(n²)
        initial_row = 0
        #start solving the first row (row: 0)
        dfs(initial_row)
        #return all valid board configurations:-
        return result    


#         | Metric    | Complexity |
# | --------- | ---------- |
# | **Time**  | **O(n!)**  |
# | **Space** | **O(n²)**  |

























        