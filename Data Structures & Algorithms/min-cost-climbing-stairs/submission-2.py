class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        # topic : 1 D DP -->
        n = len(cost)
        # Optimized space version O(1) -->
        # dp = [0] * (n)

        # Base cases
        # set dp[0] = cost[0]
        # and set dp[1] = cost[1] as our 2starting positions known via statement..
        first, second = cost[0], cost[1]

        # Fill dp array from the 3rd index to the end of the dp
        for i in range(2, n):
            # take min cost of the( dp[i-1] && dp[i-2]) add to the
            # the cost[i] for calculating the dp[i] th cost so as to calculate the
            # miniimum cost so far for dp[i]
            current = min(first, second)
            first = second
            second = cost[i] + current

        # as the start was from either 1 st or 2ns step 
        # therefore --> min cost will be stored either 
        # last or second last step bcz last could be excluded as
        # bcz from (n - 2) a step could be took to the end of 
        # of the [cost] bar..

        # time : O(N), space : O(1)
        return min(first, second)











        
        # topic : 1 D DP -->
        # n = len(cost)
        # # create a dp array-->
        # dp = [0] * (n)

        # # Base cases
        # # set dp[0] = cost[0]
        # # and set dp[1] = cost[1] as our 2starting positions known via statement..
        # dp[0], dp[1] = cost[0], cost[1]

        # # Fill dp array from the 3rd index to the end of the dp
        # for i in range(2, n):
        #     # take min cost of the( dp[i-1] && dp[i-2]) addd to the
        #     # the cost[i] for calculating the dp[i] th cost so as to calculate the
        #     # miniimum cost so far for dp[i]
        #     dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        # # as the start was from either 1 st or 2ns step 
        # # therefore --> min cost will be stored either 
        # # last or second last step bcz last could be excluded as
        # # bcz from (n - 2) a step could be took to the end of 
        # # of the [cost] bar..
        # return min(dp[n-1], dp[n-2])
