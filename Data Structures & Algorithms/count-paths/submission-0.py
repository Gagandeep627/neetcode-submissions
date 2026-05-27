class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        


        def dfs(r ,c):

            
            if (r >= m or c >= n):
                return 0


            if (r == m-1 and c == n-1):
                return 1
            




            move_possibilities = (
                # right && down-->
                dfs(r, c + 1) + dfs(r+1, c)
            )


            return move_possibilities


        ans = dfs(0,0)

        return ans