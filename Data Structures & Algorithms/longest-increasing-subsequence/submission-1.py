class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        n = len(nums)

        def helper(idx, prev):

            if (idx == (n)):
                return 0


            # skip = helper(idx + 1, prev)


            take = 0
            if (nums[idx] > prev):
                take = helper(idx + 1, nums[idx]) + 1

            skip = helper(idx + 1, prev)
            
            return (max(skip, take))

        index, prev = 0, float("-inf")
        return helper(index, prev)
        


            

