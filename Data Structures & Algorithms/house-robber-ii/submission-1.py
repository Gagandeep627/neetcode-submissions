class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n < 2:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])


        # topic : 1 D DP


        # function same concept for the house_robbing -->
        # time : O(N)
        def house_robbing(nums):

            n = len(nums)

            dp = [0] * (n)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for j in range(2, n):
                dp[j] = max(dp[j-2] + nums[j], dp[j-1])



            return dp[n-1]

    
        # case1 : take nums from 1 st to (last-1) house 
        # as this is cyclic house problem so the 1 st house is adjacent 
        # to the second last house --> as in the cyclic case 
        # if len(nums) : odd then while robing houses 1 st house cost will
        # get add up to the last house 
        # if len(nums) : even --> then in the case : 2 houses will be took from 
        #  1 st house will never coincide with the last house 
        # so, will just create to nums to include / exclude 1 st && laqst house 
        # from both the nums 1 by 1 to our house robbing functions-->
        # time : O(N)
        case1 = house_robbing(nums[:n-1])
        # time : O(N)
        case2 = house_robbing(nums[1:n])

        
        # # time : O(N), space : O(N)-->
        return max(case1, case2)




            



        