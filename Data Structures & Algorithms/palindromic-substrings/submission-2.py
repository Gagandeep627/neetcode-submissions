class Solution:
    def countSubstrings(self, s: str) -> int:

        

        # topic : brute force solns-->
        # n -- len(s)
        n = len(s)
        # count --> 0
        count = 0
        # palindromic functions-->
        def is_palindrome(sub):
            # will check whether a string is palindromic or not-->
            return sub == sub[::-1]  # simple reverse check
        
        
        # i in range(n)--> time : O(n)
        for i in range(n):
            # j in range (i -- n)--> time : O(n)
            for j in range(i, n):
                # click every substring exists for 
                # s[i:j + 1] then take a check whther is it a palindromic string or
                # not via our helper functions--> time : O(n)
                substring = s[i:j+1]
                if is_palindrome(substring):
                    # inc count += 1 if found : true-->
                    count += 1

        # ans : count
        # time : O(N ^ 3)
        return count










#         n = len(s)

#         if n < 2:
#             return 1

#         # topic : (Non DP Approach) -->
#         # 2 pointer expand around the center approach-->

#         def expand(left, right):

#             curr = 0
#             # check cond if left should be >= 0 and right should
#             # be < n && s[left] == s[right] as inside it are already been check by 
#             # so check for outside too also
#             # left += 1 pointer && right -= 1 pointer-->
             
#             while (left >= 0 and right < n and s[left] == s[right]):
#                 # if cond satisfies inc curr += 1 
#                 # expand left to left and right to right-->
#                 curr += 1
#                 left -= 1
#                 right += 1

            
#             return curr #return : curr-->


#         total = 0 # set --> 0
#         # i uptill length(n)-->
#         for i in range(n):
#             # for odd length expression palindromes -->
#             total += expand(i, i)
            
#             # for even length expression palindromes->
#             total += expand(i, i + 1)


# # Time	Each center expands up to O(n) → total 2n−1 centers → O(n²)	O(n²)
# #Total Time = O(n centers × n expansion per center) = O(n²)
# # Space	Only pointers and counters used	O(1)


        
#         return total
















        