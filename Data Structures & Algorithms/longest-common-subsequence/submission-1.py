class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        


        # topic : recursive ++ memoizations ++ solutions-->
        m = len(text1)
        n = len(text2)
        
        memo = [[-1] * n for _ in range(m)]

        def helper(i, j):

            if ((i >= len(text1)) or (j >= len(text2))):
                return 0

            if (text1[i] == text2[j]):
                memo[i][j] = 1 + helper(i+1,j+1)

            if (memo[i][j] != -1):
                return memo[i][j]


            
            max_found = max(helper(i+1,j),helper(i,j+1))

            memo[i][j] = max_found


            return memo[i][j]


        ans = helper(0,0)


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


            