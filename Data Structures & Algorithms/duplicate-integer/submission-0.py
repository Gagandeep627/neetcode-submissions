class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # time comp : O(n) -->


        samp = set()

        

        for itr in nums:

            if (itr not in samp):
                samp.add(itr)
            else:
                return True



        return False
                
                














        # time comp : O(n(log(n))) -->
        # nums.sort()

        # prev = nums[0]
        # res = False
        # for i in range(1,len(nums)):
        #         nex = nums[i]

        #         if (prev == nex):
        #             res = True
        #             return res

        #         prev = nex



        
        # return res
