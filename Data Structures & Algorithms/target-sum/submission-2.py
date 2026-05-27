class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        


        # topic : (recursive ++ memoizations solutions (top-down-dp solution)) ((reccursive - solutions)) -->

        n = len(nums)
        # n × (2m + 1) entries  →  O(n × m)
        memo = {} #Key : (i, currsum) --> value : no. of ways-->
        
        def recurse(i, curr):

            # if (i > n):
            #     return 0
            # an index i → can take n values
            # a currentSum → ranges from –m to +m, which is 2m + 1 distinct values


            # if state is already computed : return it;
            if (i, curr) in memo:
                return memo[(i, curr)]

            # base case : all no.s used
            # reached end of array-->
            if (i == n):
                if (curr == target):
                    return 1
                return 0
                
            # option 1: add nums[i]
            plus = recurse(i+1, curr + nums[i])
            # optiion 2: subtract nums[i]
            minus = recurse(i+1, curr - nums[i])

            ans = plus + minus

            memo[(i,curr)] = ans

            # So total possible unique states = n × (2m + 1)
            # O(n × m)
            return memo[(i,curr)]

#             2️⃣ Recursion stack depth

# Maximum recursion depth = n, so:

# O(n)


        
# for optimal solutions -->
#         Time Complexity:
# O(n × m)

# Space Complexity:
# O(n × m)


        start, curr = 0, 0
        return recurse(start, curr)







        # for brute force time complexity : 
#         | Approach                  | Time Complexity | Space Complexity | Why                                           |
# | ------------------------- | --------------- | ---------------- | --------------------------------------------- |
# | **Recursive brute force** | **O(2ⁿ)**       | **O(n)**         | Binary decision tree: + or – for each element |


