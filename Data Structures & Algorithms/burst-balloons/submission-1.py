class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
       
        # topic : (Recursive ++ Memoization ++ force solutions)-->
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[-1] * n for _ in range(n)]

        

        def dfs(l, r):
            
            if dp[l][r] != -1:
                return dp[l][r]

            if (l > r):
                return 0


            best = 0


            for i in range(l, r + 1):

                coins = nums[l-1] * nums[i] * nums[r+1]

                coins += dfs(l, i-1)

                coins += dfs(i+1, r)
            
                best = max(best, coins)

                dp[l][r] = best

            
            return dp[l][r]

        

        l1, r1 = 1, (n-2)

        return dfs(l1,r1)





        # # topic : (Recursive ++ Brute force solutions)-->

        # nums = [1] + nums + [1]
        # n = len(nums)

        # def dfs(l, r):

        #     if (l > r):
        #         return 0


        #     best = 0


        #     for i in range(l, r + 1):

        #         coins = nums[l-1] * nums[i] * nums[r+1]

        #         coins += dfs(l, i-1)

        #         coins += dfs(i+1, r)
            
        #         best = max(best, coins)

            
        #     return best

        

        # l1, r1 = 1, (n-2)

        # return dfs(l1,r1)


        
# ⏱️ Time and Space Complexity (Brute Force)
# Time: O(n!) (super exponential)

# Because each decision splits into many smaller subproblems.

# Space: O(n) recursion depth

        
        

        







            