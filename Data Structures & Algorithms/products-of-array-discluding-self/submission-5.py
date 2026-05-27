class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # method : 2 optimal approach --> prefix -- suffix intution of solving the problem..


        n = len(nums)
        output = [1] * (n)



        prefix = 1
        for i in range(0, n):
            output[i] = prefix
            prefix *= nums[i]



        suffix = 1
        for j in range(n-1, -1, -1):
            output[j] = output[j] * suffix
            suffix = suffix * nums[j]



        return output






            


        