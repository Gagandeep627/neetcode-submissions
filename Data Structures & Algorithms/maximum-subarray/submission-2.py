class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        # topic  kadanes' algorithm-->

        n = len(nums)

        if (n == 1):
            return nums[0]

        curr_sum = 0
        max_sum = float("-inf")


        for x in nums:
            curr_sum += x
            max_sum =  max(max_sum, curr_sum)



            if (curr_sum < 0):
                curr_sum = 0


        return max_sum


            

        

            































        # topic : recursive ++ brute force-->

        # n = len(nums)

        # def dfs(s, e):
            
        #     if (e == n):
        #         return float("-inf")

        #     curr_sum = sum(nums[s:e+1])

        #     extend_sum = dfs(s,e+1)

        #     return max(curr_sum, extend_sum)

        
        # ans = float("-inf")

        # for start in range(0, n):
        #     ans = max(ans, dfs(start, start))


        # return ans