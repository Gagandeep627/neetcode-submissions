class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        


        # topic : brute -->
        n = len(nums)
        def recurse(i, curr):

            # if (i > n):
            #     return 0

            if (i == n):
                if (curr == target):
                    return 1
                return 0
                

            plus = recurse(i+1, curr + nums[i])

            minus = recurse(i+1, curr - nums[i])

            ans = plus + minus

            return ans


        start, curr = 0, 0
        return recurse(start, curr)

