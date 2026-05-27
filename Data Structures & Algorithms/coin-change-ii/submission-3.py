class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        n = len(coins)
        dp = {} #Stores up to: n * (amount + 1)

        # i --> index , r --> remaining-->

        # topic : Recursion ++ Memoized Solutions -->
        # i ranges from 0 to n → n possible values

        # remaining ranges from 0 to amount → amount+1 possible values
        
        # Therefore, number of unique DP states;
        
        # (n) * (amount + 1)
        def recurse(i,r):
            # check memo-->
            if (i,r) in dp:
                return dp[(i,r)]

            # base cases-->
            # if remaining is 0 --> we found a valid combination
            if (r == 0):
                return 1

            #if remaining is negative --> invalid path
            if (r < 0):
                return 0


            # if no more coins left
            if (i >= n):
                return 0


                # Each state does O(1) work (just two recursive calls, both memoized).
            # take the coin (stay at same index)

            # option 1: take curent coin--> (stay at the same index) -->
            take = recurse(i, r - coins[i])
            # skip the coin (move to next index)
            # option2 : skip current coin-> (move to next index)->
            skip = recurse(i + 1, r)

            ans = take + skip

            dp[(i,r)] = ans

            # 2. Recursion call stack depth : O(amount)
            # time : O(n * amount)

            return dp[(i,r)]

#         Time Complexity (Memoized Recursion — Top-Down DP):
# O(n * amount)

# Space Complexity (Memoized Recursion — Top-Down DP):
# O(n * amount)
        
        
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



        