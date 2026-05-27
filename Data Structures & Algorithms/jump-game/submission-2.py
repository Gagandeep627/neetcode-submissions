class Solution:
    def canJump(self, nums: List[int]) -> bool:
        


        # topic : kadane's algorithm -->

        n = len(nums)
        reach = 0

        for i in range(n):

            if (i > reach):
                return False #I cannot even step here!

            if (reach >= (n-1)):
                return True

            reach = max(reach, i + nums[i])

#         Time: O(n)
# Space: O(1)




        # topic : recursive ++ brute force solutions -->
        # n = len(nums)
        # the maximum recursion depth = height of the longest jump path
        # def dfs(idx):
        # if we have reached and crossed last index-> success
        #     if (idx >= (n-1)):
        #         return True

        # O(n^n) in the worst case. if this no. cant jump anywhere->
        #     if (nums[idx] == False):
        #         return False

        # try all possible jumps from 1 -> nums[i]
        # From each choice, again up to n choices…
        #     for jump in range(1,nums[idx] + 1):
        #         if (dfs(idx + jump)): This blows up like a choice tree.
        #             return True #if any jumps works -> whole answer is true->

        # at most n recursive calls in the stack
        #     return False #all jumps failed->


        # From index 0, you may branch into up to n choices.
        # start = 0
        # return dfs(start)


        # Time: O(n^n) worst case (super exponential)
        # Space: O(n)
        


            


        