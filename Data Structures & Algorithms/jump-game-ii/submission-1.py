class Solution:
    def jump(self, nums: List[int]) -> int:



        n = len(nums)
        # topic : Optimal_Solutions (time : O(N)). : //

        jumps = 0
        current_index = 0
        farthest = 0

        for i in range(n-1):
            farthest = max(farthest, i+nums[i])

            if (i == current_index):
                jumps += 1
                current_index = farthest


        
        return jumps





































        
        # topic : brute force - Recursive solutions -->

        # n = len(nums)


        # def dfs(idx):

        #     if (idx == (n-1)):
        #         return 0

        #     if (idx >= n):
        #         return float("inf")


        #     best = float("inf")

        #     for jump_len in range(1,nums[idx] + 1):
        #         steps = 1 + dfs(idx + jump_len)
        #         best = min(best, steps)


        #     return best


        # s_index = 0

        # return dfs(s_index)

#         Time:
# O(n^n)   (exponential, extremely large)

# 🧠 Space (recursion depth):
# O(n)


        

            




        
