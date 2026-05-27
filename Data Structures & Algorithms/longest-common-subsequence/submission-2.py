class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        


        # topic : recursive ++ memoizations ++ solutions-->
        m = len(text1)
        n = len(text2)
        # Total number of unique states = m × n
#         memo[m][n]
# storing results for every (i, j).
        memo = [[-1] * n for _ in range(m)]

        def helper(i, j): #🔹 Recursion Stack: O(m + n)


            # If we reached end of either string → no subsequence
            if ((i >= len(text1)) or (j >= len(text2))):
                return 0
            
            if (text1[i] == text2[j]):# Case 1: characters match
                memo[i][j] = 1 + helper(i+1,j+1)

            if (memo[i][j] != -1):# If already solved → return stored value
                return memo[i][j]


#             Because of memoization:

# Each state is computed once

# Each state does only O(1) work besides two recursive calls 
#           # skip from text1, skip from text2 -->
            max_found = max(helper(i+1,j),helper(i,j+1))# Case 2: characters don't match → try both options

            memo[i][j] = max_found


            return memo[i][j]

        # So total time = m × n × O(1) = O(m × n)
        #Space Complexity : O(m × n + m + n) : Since m + n is much smaller, we write big-O as: O(m × n)
        ans = helper(0,0)


#         | Type      | Complexity   |
# | --------- | ------------ |
# | **Time**  | **O(m × n)** |
# | **Space** | **O(m × n)** |



        return ans





#         # topic : recursive ++ brute force recursive solutions-->


#         def helper(i, j):

#             if ((i >= len(text1)) or (j >= len(text2))):
#                 return 0

#             if (text1[i] == text2[j]):
#                 return 1 + helper(i+1,j+1)


            
#             max_found = max(helper(i+1,j),helper(i,j+1))



#             return max_found


#         ans = helper(0,0)

# #         ⏳ Time & Space Complexity (Brute Force)
# # ❌ Time = O(2^(m+n))

# # Because every mismatch creates two recursive calls → exponential.

# # ❌ Space = O(m + n)

# # Due to maximum recursion depth (at worst going down both strings).
#         return ans


            