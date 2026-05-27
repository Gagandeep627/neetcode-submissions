class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        
        # Method 1 : Brute force approach -- 
        # solution accepted hoo gaya he te better he kii
        # Move to nxt apprach for solving the problem... 

        n = len(nums)
        output = [1] * n   # Step 1: Initialize result array with 1s
        
        # Step 2: Compute prefix product for each index
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]  # keep multiplying from left
        
        # Step 3: Compute suffix product and multiply with prefix stored in output
        suffix = 1
        for i in range(n - 1, -1, -1):  # traverse from right end
            output[i] *= suffix
            suffix *= nums[i]  # keep multiplying from right
        
        return output


            


        