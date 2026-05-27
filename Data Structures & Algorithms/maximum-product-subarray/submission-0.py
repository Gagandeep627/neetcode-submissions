class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # topic : Brute Force Solutions-->
        n = len(nums)
        max_prod = float("-inf")

        for i in range(n):
            curr_pod = 1
            for j in range(i, n):
                curr_pod *= nums[j]
                max_prod = max(max_prod, curr_pod)


        return max_prod

        