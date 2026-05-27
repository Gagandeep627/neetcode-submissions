class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        # topic : 1 DP kadanes-like approach -->

        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        n = len(nums)

        for i in range(1, n):

            if (nums[i] < 0):
                max_prod, min_prod = min_prod, max_prod



            max_prod = max(nums[i], nums[i] * max_prod)

            min_prod = min(nums[i], nums[i] * min_prod)

            ans = max(ans, max_prod)


        return ans


























        # topic : Brute Force Solutions-->
#         n = len(nums)
#         max_prod = float("-inf")

#         for i in range(n):
#             curr_pod = 1
#             for j in range(i, n):
#                 curr_pod *= nums[j]
#                 max_prod = max(max_prod, curr_pod)

# #         🕒 Time Complexity:

# # Outer loop (start i): n

# # Inner loop (end j): up to n

# # So total = O(n²)
# # (since for each i, we multiply at most n-i elements)

# # 💾 Space Complexity:

# # We only use a few variables → O(1)
#         return max_prod

        