class Solution:
    def maxSubArray(self, nums: List[int]) -> int:



        # topic : recursive ++ brute force-->

        n = len(nums)

        def dfs(s, e):
            
            if (e == n):
                return float("-inf")

            curr_sum = sum(nums[s:e+1])

            extend_sum = dfs(s,e+1)

            return max(curr_sum, extend_sum)

        
        ans = float("-inf")

        for start in range(0, n):
            ans = max(ans, dfs(start, start))


        return ans