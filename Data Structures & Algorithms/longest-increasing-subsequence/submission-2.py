class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # topic : recursive ++ brute force solutions-->  
        n = len(nums)

        memo = [[-1] * (n + 1) for _ in range(n)]

        def helper(idx, prev):

            if (idx == (n)):
                return 0

            if (memo[idx][prev + 1] != -1):
                return memo[idx][prev + 1]
            # skip = helper(idx + 1, prev)

            take = 0
            if ((nums[idx] > nums[prev]) or (prev == -1)):
                take = helper(idx + 1, idx) + 1

            skip = helper(idx + 1, prev)
            
            memo[idx][prev + 1] = (max(skip, take))

            return memo[idx][prev + 1]



        index, prev = 0, -1

        return helper(index, prev)


































        # # topic : recursive ++ brute force solutions-->  
        # n = len(nums)

        # def helper(idx, prev):

        #     if (idx == (n)):
        #         return 0


        #     # skip = helper(idx + 1, prev)

        #     take = 0
        #     if (nums[idx] > prev):
        #         take = helper(idx + 1, nums[idx]) + 1

        #     skip = helper(idx + 1, prev)
            
        #     return (max(skip, take))

        # index, prev = 0, float("-inf")
        
        # return helper(index, prev)
        


            

