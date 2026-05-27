class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        n = len(coins)
        dp = {}

        # i --> index , r --> remaining-->

        # topic : Recursion ++ Brute force Solutions -->

        def recurse(i,r):

            if (i,r) in dp:
                return dp[(i,r)]

            if (r == 0):
                return 1

            if (r < 0):
                return 0

            if (i >= n):
                return 0
            # take the coin (stay at same index)
            take = recurse(i, r - coins[i])
            # skip the coin (move to next index)
            skip = recurse(i + 1, r)

            ans = take + skip

            dp[(i,r)] = ans

            return dp[(i,r)]

        
        
        
        start, remaining = 0, amount

        return recurse(start, remaining)






#         n = len(coins)

#         # i --> index , r --> remaining-->

#         # topic : Recursion ++ Brute force Solutions -->

#         def dfs(i,r):

#             if (r == 0):
#                 return 1

#             if (r < 0):
#                 return 0

#             if (i >= n):
#                 return 0
#             # take the coin (stay at same index)
#             take = dfs(i, r - coins[i])
#             # skip the coin (move to next index)
#             skip = dfs(i + 1, r)

#             ans = take + skip

#             return ans

#         # This generates an exponential recursion tree.
# # Worst case:
# # Amount is large (5000)
# # Coins include 1 (so we can “take” many times)
# # Recursion depth on “take” branch can be amount / coin[i]
# # This forms a binary recursion tree with deep “take” branches.
# # ⭐ Precise Time Complexity : O(2^(amount + number_of_coins))
#         # ⭐ Time = O(2^(amount / min_coin))

#         # 🟥 Time = O(2^amount)

#         # ⭐ Space Complexity : O(amount)
        
        
#         start, remaining = 0, amount

#         return dfs(start, remaining)



        