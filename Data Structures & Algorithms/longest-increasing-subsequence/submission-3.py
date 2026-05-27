class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # topic : recursive ++ brute force solutions -->
        # (top-down memoization solutions)-->  
        
        
        n = len(nums)
        # dp[i][prev+1] → memo table
        # prev goes from -1 to n-1, so use prev+1 to make it 0-based
        memo = [[-1] * (n + 1) for _ in range(n)]

        def helper(idx, prev):
             # if we reached end → LIS length is 0
            if (idx == (n)):
                return 0
            # check memo
            if (memo[idx][prev + 1] != -1):
                return memo[idx][prev + 1]
            # skip = helper(idx + 1, prev)
            # OPTION 1 → take nums[i] (if allowed)
            take = 0
            if ((nums[idx] > nums[prev]) or (prev == -1)):
                take = helper(idx + 1, idx) + 1
            #  # OPTION 2 → skip nums[i]
            skip = helper(idx + 1, prev)
            # store the best
            memo[idx][prev + 1] = (max(skip, take))

            return memo[idx][prev + 1]



        index, prev = 0, -1



#         | Metric               | Complexity |
# | -------------------- | ---------- |
# | **Time Complexity**  | **O(n²)**  | Where:

# i can take n different values → 0 to n-1

# prevIndex can take n+1 different values → from -1 to n-1
# (stored as 0 to n in DP)

# So total number of unique states =

# n * (n + 1)  ≈  n²
# | **Space Complexity** | **O(n²)**  |

# start from index 0, with prev = -1 (means nothing taken yet)
        return helper(index, prev)


































        # # topic : recursive ++ brute force solutions-->  
        # n = len(nums)

        # def helper(idx, prev):

        # BASE CASE: no elements remain
        #     if (idx == (n)):
        #         return 0

        # # OPTION 1: skip nums[i]
        #     # skip = helper(idx + 1, prev)
        # OPTION 2: take nums[i] if allowed
        #     take = 0
        #     if (nums[idx] > prev):
        #         take = helper(idx + 1, nums[idx]) + 1

        #     skip = helper(idx + 1, prev)
        # Return best of both
        #     return (max(skip, take))

        # index, prev = 0, float("-inf")
        # Start from index 0, with prev = -infinity
        # return helper(index, prev)
        


            

