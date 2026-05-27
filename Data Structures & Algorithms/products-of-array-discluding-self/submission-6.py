class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # method : 2 optimal approach --> prefix -- suffix intution of solving the problem..


        n = len(nums)
        output = [1] * (n)


        # calculated prefix for every integer in
        #  the output array then prefix is changed to (nums[i] * prefix) : O(n)
        prefix = 1
        for i in range(0, n):
            output[i] = prefix
            prefix *= nums[i]



        # calculated suffix for every 
        # output[n : starting for last -- start element..(k th index)] = output[k] * suffix
        # suffix --> changed to suffix * nums[j] :O(n)
        suffix = 1
        for j in range(n-1, -1, -1):
            output[j] = output[j] * suffix
            suffix = suffix * nums[j]




        # time complex : O(N)..
        # space complex : O(N)



        return output






            


        