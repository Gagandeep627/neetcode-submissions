class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        


        # topic : brute-force (reccursive - solutions) -->

        n = len(nums)

        memo = {}
        


        def recurse(i, curr):

            # if (i > n):
            #     return 0

            if (i, curr) in memo:
                return memo[(i, curr)]

            if (i == n):
                if (curr == target):
                    return 1
                return 0
                

            plus = recurse(i+1, curr + nums[i])

            minus = recurse(i+1, curr - nums[i])

            ans = plus + minus

            memo[(i,curr)] = ans

            return memo[(i,curr)]


        start, curr = 0, 0
        return recurse(start, curr)

