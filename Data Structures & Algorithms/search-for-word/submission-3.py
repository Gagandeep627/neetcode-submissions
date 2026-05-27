class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # topic : backtracking. ++ : ++ ??
        def dfs(r, c, i):
            # base case when i == len(word) : the True;
            if i == len(word):
                return True

            # when r && c are out of bounds or when (board[r][c] != word[i]):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]):
                return False

            # mark cells as visited and store that value in temp..
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all directions -->
            found = (
                dfs(r + 1, c, i + 1) or  # row down --> down to the cell..
                dfs(r - 1, c, i + 1) or # row up --> up to the cell..
                dfs(r, c + 1, i + 1) or  # right to the cell..
                dfs(r, c - 1, i + 1)     # left to cell..
            )

            # then backtrack and mark the unmark cells-->
            board[r][c] = temp

            return found

        # try every (row, cols) check for board[r][c] == word[0]
        # to check if the first letters matches 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:  
                    if dfs(r, c, 0): # function call__ dfs(r, c, 0):
                        return True # return true if all elements compute to the
                        # to the up, down , right && left to the matrix if matches to the 
                        # to word[i]-->


        # Total time=O(m×n×4L)
        # Hence, Auxiliary Space = O(L)
        return False
        