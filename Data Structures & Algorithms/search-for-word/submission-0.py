class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # ✅ Base case: all letters found
            if i == len(word):
                return True

            # 🚫 Out of bounds or mismatch
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]):
                return False

            # 🌀 Mark cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all 4 directions
            found = (
                dfs(r + 1, c, i + 1) or  # down
                dfs(r - 1, c, i + 1) or  # up
                dfs(r, c + 1, i + 1) or  # right
                dfs(r, c - 1, i + 1)     # left
            )

            # ♻️ Backtrack (unmark cell)
            board[r][c] = temp

            return found

        # 🔍 Try every cell as a starting point
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:  # first letter matches
                    if dfs(r, c, 0):
                        return True

        return False
        