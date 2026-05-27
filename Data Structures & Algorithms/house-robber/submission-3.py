class Solution:
    def rob(self, nums: List[int]) -> int:

        # topic : 1 D - DP array-->
        n = len(nums)

        if n <= 2:
            return max(nums)
        # space : O(n)
        dp = [0] * (n)
        # at 0 th we can only rob 0 th house-->
        dp[0] = nums[0]
        # at 1 th we can only rob from either 0, 1 th house-->
        dp[1] = max(nums[0], nums[1])


        # time : O(n)
        for i in range(2, n):
            # dp call formula for such house robbery-->
            # either current house nums[i] with house the house not adjacent to 
            # it say (i - 2) or take house only its adjacent house but we cant take 
            # both house , exculde both of them and take max(dp[i-1], house(i) + dp[i-2])
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])


        # return fp[last house : will]
        # point out to the maximum amount could be robbed from 
        # non adjacent houses-->
        return dp[n-1]


    
        