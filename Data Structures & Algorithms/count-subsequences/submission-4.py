class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # topic : recursive ++ memoized force solutions -->

        memo = {}

        def dfs(i, j):

            if (i,j) in memo:
                return memo[(i,j)]

            if (j == len(t)):
                return 1
            
            if (i == len(s)):
                return 0

            ways = 0
            # Every character of s branches into skip and take
            if (s[i] == t[j]):
                ways += dfs(i+1,j+1)


            ways += dfs(i+1,j)

            memo[(i,j)] = ways

            return ways

        
        start1, start2 = 0,0
        
        # Recursion depth = length of s: ⭐ O(m)
        return dfs(start1, start2)




















        


        # ⏱️ Time Complexity (Brute Force)

# Worst case:

# Every character of s branches into skip and take

# So:

# ⭐ O(2^m)

# (Where m = len(s). Exponential.)

# 🧵 Space Complexity

# Recursion depth = length of s:

# ⭐ O(m)
        