class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        # topic : recursive ++ memoization ++ DP (brute-force-solutions) -->
        memo = {}

        def helper(i, memo):
            # we can skip step 1 or step 2 as per nums index will
            # reflect to indexes :(0, 1).
            if i <= 1:
                return 0
            
            # if i already in memo : return the stored result from memo
            if (i in memo):
                return memo[i]

            # memo[index : i] = 
            # goo 1 step ahead + take its cost : helper(i - 1, memo) + cost[i - 1]
            # goo 2 step ahead + take its cost : helper(i - 2, memo) + cost[i-2]
            # take min(step1, step2) and store to index : i
            # of memo to --> memo[i]
            memo[i] = min(helper(i - 1, memo) + cost[i - 1], helper(i - 2, memo) + cost[i-2])

            
            # return : our calculated to memo[key = index : i] to helper function
            # in order to calculate for further steps to the helper(other1 , 2 s step possible so far)
            # along with their cost values as parametrized..
            return memo[i]

        n = len(cost)
        # helper(n:length of the nums, memo : dict)
        res = helper(n, memo) # ans = res

#         🧮 Time and Space Complexity for memoization-->
# Complexity	Value	Reason
# Time	O(n)	Each step (0→n) is computed once, memoization avoids recomputation.
# Space	O(n)	Due to recursion stack + memo dictionary storing results.

# 🧮 Step 5: Time and Space Complexity (Precisely)
# Type	Complexity	Explanation
# Time Complexity	O(2ⁿ)	Each step can branch into 2 calls → exponential growth
# Space Complexity	O(n)	Maximum recursion depth (call stack)
        
        return res

        
            
            


























        # n = len(cost)
        # # Optimized space version O(1) -->
        # # dp = [0] * (n)

        # # Base cases
        # # set dp[0] = cost[0]
        # # and set dp[1] = cost[1] as our 2starting positions known via statement..
        # first, second = cost[0], cost[1]

        # # Fill dp array from the 3rd index to the end of the dp
        # for i in range(2, n):
        #     # take min cost of the( dp[i-1] && dp[i-2]) add to the
        #     # the cost[i] for calculating the dp[i] th cost so as to calculate the
        #     # miniimum cost so far for dp[i]
        #     current = min(first, second)
        #     first = second
        #     second = cost[i] + current

        # # as the start was from either 1 st or 2ns step 
        # # therefore --> min cost will be stored either 
        # # last or second last step bcz last could be excluded as
        # # bcz from (n - 2) a step could be took to the end of 
        # # of the [cost] bar..

        # # time : O(N), space : O(1)
        # return min(first, second)











        
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
