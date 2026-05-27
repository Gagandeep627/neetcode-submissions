class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        # topic : recurse ++ memoized version intuition-->
        # space : m×n
        # memoarray intialized with -1
        memo = [[-1] * n for _ in range(m)]

        def dfs(r ,c):

            # if out of grid -> no path
            if (r >= m or c >= n):
                return 0

            # if reached bototm-right -> 1 path
            if (r == m-1 and c == n-1):
                return 1
            # if already cmputed right--> path..
            if (memo[r][c] != -1):
                return memo[r][c]
            
            #if already computed ->return memoized value..
            move_possibilities = (
                # right && down-->
                dfs(r, c + 1) + dfs(r+1, c)
            )

            # ✔ Every state (r, c) is computed once
            # m×n distinct states
            # explore down and right-->
            memo[r][c] = move_possibilities


#             Each state does O(1) work:

# 2 recursive calls

# constant-time memo lookup
            return memo[r][c]


            # return move_possibilities
        
        # time : O(m×n)

        ans = dfs(0,0)


#         | Complexity Type      | Precise Value | Reason                         |
# | -------------------- | ------------- | ------------------------------ |
# | **Time Complexity**  | **O(mn)**     | Each state `(r,c)` solved once |
# | **Space Complexity** | **O(mn)**     | Memo table + recursion stack  (stack space=O(m+n) + O(mn)​)   |
            


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