class Solution:
    def canJump(self, nums: List[int]) -> bool:
        


        # topic : kadane's algorithm -->

        n = len(nums)
        reach = 0

        for i in range(n):

            if (i > reach):
                return False

            if (i >= (n-1)):
                return True

            reach = max(reach, i + nums[i])



































        # topic : recursive ++ brute force solutions -->
        # n = len(nums)

        # def dfs(idx):

        #     if (idx >= (n-1)):
        #         return True

            
        #     if (nums[idx] == False):
        #         return False


        #     for jump in range(1,nums[idx] + 1):
        #         if (dfs(idx + jump)):
        #             return True

            
        #     return False


        
        # start = 0
        # return dfs(start)
        


            


        