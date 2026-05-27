class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # topic : brute force - Recursive solutions -->

        n = len(nums)


        def dfs(idx):

            if (idx == (n-1)):
                return 0

            if (idx >= n):
                return float("inf")


            best = float("inf")

            for jump_len in range(1,nums[idx] + 1):
                steps = 1 + dfs(idx + jump_len)
                best = min(best, steps)


            return best


        s_index = 0

        return dfs(s_index)


        

            




        
