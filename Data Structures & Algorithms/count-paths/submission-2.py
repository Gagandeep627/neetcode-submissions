class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        # topic : recurse ++ memoized version intuition-->

        memo = [[-1] * n for _ in range(m)]

        def dfs(r ,c):

            
            if (r >= m or c >= n):
                return 0


            if (r == m-1 and c == n-1):
                return 1

            if (memo[r][c] != -1):
                return memo[r][c]
            
        
            move_possibilities = (
                # right && down-->
                dfs(r, c + 1) + dfs(r+1, c)
            )


            memo[r][c] = move_possibilities

            return memo[r][c]


            # return move_possibilities


        ans = dfs(0,0)            


        return ans







# topic : recurse ++ bruce intuition logic->
#         def dfs(r ,c):

            
#             if (r >= m or c >= n):
#                 return 0


#             if (r == m-1 and c == n-1):
#                 return 1
            




#             move_possibilities = (
#                 # right && down-->
#                 dfs(r, c + 1) + dfs(r+1, c)
#             )


#             return move_possibilities


#         ans = dfs(0,0)


# #         | Complexity Type | Value          | Reason                                              |
# # | --------------- | -------------- | --------------------------------------------------- |
# # | **Time**        | **O(2^(m+n))** | 2 choices at each step → exponential recursion tree |
# # | **Space**       | **O(m+n)**     | recursion depth equals number of moves              |


#         return ans