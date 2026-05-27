class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        # topic  kadanes' algorithm : time : O(n)-->

        n = len(nums)

        if (n == 1):
            return nums[0]

        curr_sum = 0
        max_sum = float("-inf")

        # We scan the array only once from left to right.
        for x in nums:
            curr_sum += x #add x to the current bag
            # At each index, we do constant-time operations (just comparisons and additions).
            max_sum =  max(max_sum, curr_sum)


            # So total work = n × O(1) = O(n).
            if (curr_sum < 0): #bag becomes harmful -> dump it.
                curr_sum = 0

        # Time Complexity is O(n) because we perform a single linear pass through the array.
        return max_sum

#         We use only two variables:

# current_sum

# max_sum 📦 Space Complexity: O(1)


            

        

            































        # topic : recursive ++ brute force-->

        # n = len(nums)
        # recursive functions -> sum of subarray nums[start : end + 1]
        # def dfs(s, e):
        # Reason:

        # There are O(n²) subarrays
            
        #     if (e == n):
        #         return float("-inf") #invalid so return very small value
        # Each time we compute sum(...) which is O(n)
        # option 1 : take the current element and extend the subarray-->
        #     curr_sum = sum(nums[s:e+1])
            # Due to recursion depth ≤ n
            # option 2: extend the subarray further to the right-->
        #     extend_sum = dfs(s,e+1) Space Complexity = O(n)
        # best between stopping or extending ->
        #     return max(curr_sum, extend_sum)

        
        # ans = float("-inf")
        
        # try all possible starting points-->
        # for start in range(0, n):
        #     ans = max(ans, dfs(start, start))

        # Total = n² * n = n³
        # return ans