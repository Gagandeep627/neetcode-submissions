class Solution:
    def longestPalindrome(self, s: str) -> str:


        # topic : 2 pointer (expansion around center)-->
        n = len(s)
        # return same string if n <= 1-->
        if (n <= 1):
            return s

        def expand(left, right):
            # basic :check condition for palindromic string
            # and checking for left >= 0 and right < n-->
            while (left >= 0 and right < n and s[left] == s[right]):
                left -= 1
                right += 1
            
            # return : (left + 1, right - 1)
            return (left+1, right-1)

        # set start : 0, end : 0-->
        start, end = 0, 0

        for i in range(n):
            # expand for odd circle-->
            l1, r1 = expand(i, i)
            # expand for even circle-->
            l2, r2 = expand(i, i + 1)
            # check if greater (l1, l2) && (r1, r2) -->
            # values are found for (start, end) then set that values to (start, end)-->
            if (r1 - l1) > (end - start):
                start, end = l1, r1
            if (r2 - l2) > (end - start):
                start, end = l2, r2

            # return s[start : end + 1] = answer = res-->
#             Time	O(n²)	For each of n centers, expansion can go up to n
# Space	O(1)	Only variables start, end, and temp pointers
        return s[start : end+1]






















        # topic : brute force solution (recursive-solns)-->

#         def is_palindromic(l, r):

#             while (l < r):
#                 if (s[l] != s[r]):
#                     return False
#                 l += 1
#                 r -= 1


#             return True

            


#         def helper(start, end):

#             if (start > end):
#                 return ""


#             if is_palindromic(start, end):
#                 return s[start: end + 1]

            
#             left = helper(start+1, end)

#             right = helper(start, end-1)

#             return left if len(left) > len(right) else right
            




#         n = len(s)
#         res = helper(0, n-1)

# #         Type	Explanation	Complexity
# # Time	There are O(n²) substrings, and each isPalindrome check takes O(n).	O(n³)
# # Space	Recursion depth = O(n), and no extra data structure used.	O(n)


#         return res




        # n --> length of s-->
        # topic : 2 D DP array for resolutions-->
        # n = len(s)
        
        # # mark first each every letter of the dp matrix to be the False-->
        # dp = [[False] * n for _ in range(n)]

        # # mark each and every individual letter of the (s) to be palindromic -->
        # # dp[i][i] = True-->
        # for i in range(n):
        #     dp[i][i] = True

        # start, max_len = 0, 1
        # # start length from 2 --> (n + 1) time :O(n)
        # for length in range(2, n + 1):
        #     # move i from 0 --> (n - length + 1) to upto which i can move for 
        #     # for checking string to be palindromic for required length-->
        #     # time : O(n)
        #     for i in range(n - length + 1):
        #         # calc : j last element for the substring : 
        #         # j = (start  to length - 1) to calc index for
        #         # for a substring of the appropriate length-->
        #         j = (i + length - 1)

        #         # check first && last index are same or not..
        #         # and if length of the substring is 2 or 
        #         # or subtstring in btw the sttring is also palindromic or not?
        #         if ((s[i] == s[j]) and ((length == 2) or (dp[i+1][j-1] == True))):
        #             # if condn. matches --> check dp[i][j] = True-->
        #             dp[i][j] = True
        #             # mark start --> i
        #             start = i
        #             # mark max_len to the max_length -->
        #             # via this condn..
        #             if (max_len <= length):
        #                 max_len = length



        # # mmaximum possible palindromic substring :
        # # substring : s[start : start + max_len]-->
        # # time : O(n ^ 2);
        # # space : O(n ^ 2);
        # return s[start:start + max_len]


        
        