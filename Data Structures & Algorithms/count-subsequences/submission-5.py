class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # topic : recursive ++ memoized (top-down dp solutions) force solutions : -->
        # Because (i, j) states = len(s) * len(t)
        memo = {} # creations of memo : cache->

        def dfs(i, j):
            
            # check memo->
            # Each state computed once.
            if (i,j) in memo:
                return memo[(i,j)]

            # if we have matched all of t -> valid subsequence->
            if (j == len(t)):
                return 1
            # if s is finished but t is not -> no more ways->
            if (i == len(s)):
                return 0

            ways = 0
            # Every character of s branches into skip and take

            # option 1-> matcjh these  characters-->
            # if characters match, try using s[i]->
            if (s[i] == t[j]):
                ways += dfs(i+1,j+1)

            # option 2-> skip s[i]
            ways += dfs(i+1,j)


            # Every character of s branches into skip and take
            # time : O(n × m)
            memo[(i,j)] = ways

            # Memo + recursion stack : Space = O(n × m)
            return ways

        
        start1, start2 = 0,0
        
        # Recursion depth = length of s: ⭐ O(m)
        return dfs(start1, start2)

#         Time = O(n × m)

# Because (i, j) states = len(s) * len(t)
# Each state computed once.

# Space = O(n × m)

# Memo + recursion stack.



# for brute force -->
# time : O(2^m)
# space : Recursion depth = length of s:⭐ O(m)




















        # ⏱️ Time Complexity (Brute Force)

# Worst case:

# Every character of s branches into skip and take

# So:

# ⭐ O(2^m)

# (Where m = len(s). Exponential.)

# 🧵 Space Complexity

# Recursion depth = length of s:

# ⭐ O(m)
        