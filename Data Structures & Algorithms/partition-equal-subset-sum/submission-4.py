class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        
        # topic : recursive ++ memoizations solutions-->


        total = sum(nums)
        # If total sum is odd, you can never split it into two equal parts
        if (total % 2 != 0):
            return False

        target = total // 2
        # O(n * target)
        memo = {}
        # Recursion: try to form "target" using nums starting from index i
        def recurse(i, currsum):

#             Where:

# i ranges from 0 to n-1 → n possible values
            if (currsum == target): # If current sum equals target → success
                return True
            # currSum ranges from 0 to target → target + 1 values
            # Total states = n * (target + 1)
            # If we reached end OR currSum exceeded target → fail
            if (i == len(nums) or (currsum > target)):
                return False

            # For each state, the recursion does O(1) work (just checking memo, two calls, storing result).
            if (i, currsum) in memo:
                return memo[(i,currsum)]

            # option 1 : take--> # OPTION 1: Take nums[i]
            take = recurse(i + 1, currsum + nums[i])

            # OPTION 2: Skip nums[i]
            skip = recurse(i + 1, currsum)

            # For each state, the recursion does O(1) work (just checking memo, two calls, storing result).
            if (take):
                memo[(i,currsum)] =  take # as take --> True so you can return take or True any of it you want-->
            else:
                memo[(i,currsum)] =  skip

            return memo[(i,currsum)]

        # O(n * target) : O(n * (totalSum / 2))  →  O(n * totalSum) -> O(n * t) where t = target.
        ans = recurse(0, 0)


# 🟢 Time & Space Complexity (Precise)
# Let:

# n = len(nums)

# t = target = total/2

# Time Complexity
# O(n * t)


# Because every (i, currSum) pair is computed once and memoized.

# Space Complexity
# O(n * t)   # memo table + recursion stack

       
        return ans





























        # # topic : recursive ++ brute force recursive solutions-->


        # total = sum(nums)

        # if (total % 2 != 0):
        #     return False

        # target = total // 2



        # def recurse(i, currsum):


        #     if (currsum == target):
        #         return True
            
        #     if (i == len(nums) or (currsum > target)):
        #         return False


        #     # option 1 : take-->
        #     take = recurse(i + 1, currsum + nums[i])

            

        #     skip = recurse(i + 1, currsum)

        #     if (take):
        #         return take # as take --> True so you can return take or True any of it you want-->
        #     else:
        #         return skip

        
        # ans = recurse(0, 0)



        # #         🔥 Time: O(2^n)

        # # Because it explores ALL subsets.

        # # 🔥 Space: O(n)

        # # Because recursion depth = n.
        # return ans






























    