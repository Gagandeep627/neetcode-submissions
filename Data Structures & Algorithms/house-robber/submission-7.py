class Solution:
    def rob(self, nums: List[int]) -> int:


        # topic : recursive ++ brute_recursive_solutions-->
        # top-down dp approach
        # memoization approach-->
        n = len(nums)
        if (n < 1):
            return 0

        if (n == 1):
            return nums[0]

        dp = {}

        def robbing(nums, i):

            # base case 1: out of bounds for index->
            if (i >= len(nums)):
                return 0
            # if i already stored in the dp then return the stored result : dp[i]
            if (i in dp):
                return dp[i]

            # either rob the nums[current] && skip the
            # the next next house as per question conditions--> 
            rob_curr = (robbing(nums, i+2) + nums[i])

            # another house : leave the current house and 
            # rob the next house bcz alternatively houses will be robbed 
            # so that we will leave the previous and house next to it.. 
            skip_curr = robbing(nums, i+1)

            # store the max(robing current, skipping current) -->
            # store it to dp[i]
            # return dp[i] which is our result..
            dp[i] = max(rob_curr, skip_curr)

            return dp[i]
      
        # set index --> 0 , return : result-->
        res = robbing(nums, 0)
        return res
        


























        # topic : 1 D - DP array-->
        # n = len(nums)

        # if n <= 2:
        #     return max(nums)
        # # space : O(n)
        # dp = [0] * (n)
        # # at 0 th we can only rob 0 th house-->
        # dp[0] = nums[0]
        # # at 1 th we can only rob from either 0, 1 th house-->
        # dp[1] = max(nums[0], nums[1])


        # # time : O(n)
        # for i in range(2, n):
        #     # dp call formula for such house robbery-->
        #     # either current house nums[i] with house the house not adjacent to 
        #     # it say (i - 2) or take house only its adjacent house but we cant take 
        #     # both house , exculde both of them and take max(dp[i-1], house(i) + dp[i-2])
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1])


        # # return fp[last house : will]
        # # point out to the maximum amount could be robbed from 
        # # non adjacent houses-->
        # return dp[n-1]


    
        