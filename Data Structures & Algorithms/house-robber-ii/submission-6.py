class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        memo = {}
        # topic : recursive (brute-force-solutions)-->


        if (n < 1):
            return 0
        
        if (n == 1):
            return nums[0]


        def helper(nums, i, memo):
            

            if (i >= len(nums)):
                return 0

            if (i in memo):
                return memo[i]


            curr_rob = (nums[i] + helper(nums,i + 2, memo))

            skip_rob = (helper(nums, i + 1, memo))


            memo[i] = max(curr_rob, skip_rob)

            return memo[i]

            
        


        

        case1 = helper(nums[:n-1], 0, {})

        case2 = helper(nums[1:n], 0, {})


#         | Type                 | Complexity | Explanation                                                                           |
# | -------------------- | ---------- | ------------------------------------------------------------------------------------- |
# | **Time Complexity**  | **O(2ⁿ)**  | Because each recursive call branches into two (`rob` or `skip`) — exponential growth. |
# | **Space Complexity** | **O(n)**   | Maximum recursion depth for `n` houses (call stack).                                  |

        return max(case1, case2)




            



        