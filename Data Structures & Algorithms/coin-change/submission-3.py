class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # self.total = float("inf")

        # topic : DP solutions-->


        dp = [float("inf")] * (amount + 1)

        dp[0] = 0



        for amt in range(1, amount + 1):
            for coin in coins:
                if ((amt - coin) >= 0):
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])




        return -1 if dp[amount] == float("inf") else dp[amount]

































        # topic : brute force solution-->
        def helper(cns, amt):

            if (amt == 0):
                return 0
            
            if (amt < 0):
                return float("inf")



            ans = float("inf")
            for cn in cns:

                res = helper(coins, amt - cn)
                if res != float('inf'):
                    ans = min(ans, 1 + res)


            return ans

        res = helper(coins, amount)

        return res if res != float("inf") else -1


        