class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        # topic : recursive ++ memoizations-->
        # top-down DP solutions-->

        memo = {}

        def helper(i, memo):

            if i < 2:
                return 1
            
            if i in memo:
                return memo[i]

            memo[i] = helper(i-1, memo) + helper(i-2, memo)

            return memo[i]

        res = helper(n, memo)


#         Time Complexity:
# Each call branches into 2 more calls → exponential growth.
# So,O(2n)

        return res




























        # space optimized : O(1) -->
        # if (n <= 2):
        #     return n
        
        # first, second = 1, 2 # Base cases

        # #first → ways to reach (i−2)
        # # second → ways to reach (i−1)
        # # current = first + second
        # # first = second
        # #second = current
         
        # for i in range(3, n + 1):
        #     first, second = second, (first + second)

        # return second

        # Time Complexity
# One loop runs n-2 times
# O(n)

#Space Complexity
# Only 2 integer variables (first, second)
# O(1)









        # Base cases
        # if (n <= 2):
        #     return n
        # # 1-D DP array
        # dp = [0] * (n + 1)


        # dp[0] = 1
        # dp[1] = 2

        # # Build up from step 3 to n
        # for i in range(2, n+1):
        #     dp[i] = (dp[i-1] + dp[i-2])


        
        # return dp[n-1]
        