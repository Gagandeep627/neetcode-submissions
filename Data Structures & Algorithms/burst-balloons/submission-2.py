class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
       
        # topic : (Recursive ++ Memoization ++ force solutions)-->
        # add 1 at both ends.
        nums = [1] + nums + [1]
        n = len(nums)

        # dp[l][r] = max coins from bursting ballons in the interval (l..r)
        dp = [[-1] * n for _ in range(n)] # 1. Memo Table (DP):

# dp[l][r] is an n × n 2D array: O(n²)

        
        # burst ballons in the intervals of (l, r)-->
        def dfs(l, r):
            # Each subproblem is defined by the range (l, r) where: 1 ≤ l ≤ r ≤ n-2
            if dp[l][r] != -1:
                return dp[l][r]

                # Therefore, number of unique states: ≈ (n²)/2  → O(n²)
            # if no ballon in this range : is present therefore-->
            if (l > r):
                return 0


            best = 0

            # Work per Subproblem:
            # For each (l, r), we try all possible balloons i in the range: l ≤ i ≤ r
            # i is the last ballon to be burst in this range
            # i shall go from right from ((l) -- > (r+1))
            # it will burst one by one the nums[i]
            # for each i we evaluate all possible combinations with 
            # left : (0 --> i) and right : (i+1 --> (len(nums+1))
            # and after such actions coins is being evaulated as per all possibilities existed so far...
            # uptill that coins is being calculated which will satisfies the maximum
            # for the best assigned to --> 0 for each new and unqeue path starting 
            # from nums[0] --> for each (i th position) its left : dfs() calls result 
            # and right = dfs() --> so for maxium coins possible so far for the i th burst out space is evaluated
            # and then after that best is evaluated -->
            # returned : best (INT) value is our answer
            # i is the balllon to be burst last->
            for i in range(l, r + 1):
                # That costs: O(r - l + 1)  → O(n)

                # burst i last --> its neighbors ae fixed nums[l-1] and nums[r+1]
                coins = nums[l-1] * nums[i] * nums[r+1]

                # solve the left and right subranges
                coins += dfs(l, i-1) #left subrange

                coins += dfs(i+1, r) #right subrange

                # take maximum over all characters
                best = max(best, coins)

                # Thus total time: O(n² states) × O(n work per state) = O(n³)
                dp[l][r] = best


                # 2. Recursion Stack:

                #     Worst case depth:

                #         O(n)


                #     This does not dominate the dp table.

            
            return best

#             Thus total space:

# O(n²) + O(n)  → O(n²)

# ✔ Final Space Complexity: O(n²)

        

        l1, r1 = 1, (n-2)

        return dfs(l1,r1)

#         Time Complexity:

# O(n³)


# Space Complexity:

# O(n²)





        # # topic : (Recursive ++ Brute force solutions)-->

        # nums = [1] + nums + [1]
        # n = len(nums)

        # def dfs(l, r):

        #     if (l > r):
        #         return 0


        #     best = 0


        #     for i in range(l, r + 1):

        #         coins = nums[l-1] * nums[i] * nums[r+1]

        #         coins += dfs(l, i-1)

        #         coins += dfs(i+1, r)
            
        #         best = max(best, coins)

            
        #     return best

        

        # l1, r1 = 1, (n-2)

        # return dfs(l1,r1)


        
# ⏱️ Time and Space Complexity (Brute Force)
# Time: O(n!) (super exponential)

# Because each decision splits into many smaller subproblems.

# Space: O(n) recursion depth

        
        

        







            