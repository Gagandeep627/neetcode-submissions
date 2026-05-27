class Solution:
    def jump(self, nums: List[int]) -> int:



        n = len(nums)
        # topic : Optimal_Solutions (time : O(N)). : //

    #O(1)​
        jumps = 0
        current_index = 0
        farthest = 0

        for i in range(n-1): #We iterate through the array once, from index 0 to n-2.
            farthest = max(farthest, i+nums[i])#O(1)​

            if (i == current_index): #Every index is processed exactly one time.
                jumps += 1
                current_index = farthest#O(1)​


        # No nested loops, no backtracking, no recursion. time : O(n)​. : //
        return jumps

#         | Complexity Type | Value    |
# | --------------- | -------- |
# | **Time**        | **O(n)** |
# | **Space**       | **O(1)** |







        # topic : brute force - Recursive solutions -->

        # n = len(nums)

        # Brute force recursion is very slow — that’s expected. : Space (recursion depth):O(n)
        # def dfs(idx):
        # if we have the last index -> no more jumps needed-->
        #     if (idx == (n-1)):
        #         return 0
        # if we go beyond  array (invalid), return a very large no.
        #     if (idx >= n):
        #         return float("inf")

        # try all jumps from 1 -> nums[i]
        #     best = float("inf")
        # Every index tries up to n jumps
        #     for jump_len in range(1,nums[idx] + 1): Total states ~ n, branching factor ~ n
        #         steps = 1 + dfs(idx + jump_len) #O(n^n) -> take 1 jump -> solve rest   (exponential, extremely large)
        #         best = min(best, steps)


        #     return best


        # s_index = 0

        # return dfs(s_index)

#         Time:
# O(n^n)   (exponential, extremely large)

# 🧠 Space (recursion depth):
# O(n)


        

            




        
