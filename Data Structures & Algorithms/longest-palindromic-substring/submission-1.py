class Solution:
    def longestPalindrome(self, s: str) -> str:

        # n --> length of s-->
        # topic : 2 D DP array for resolutions-->
        n = len(s)
        
        # mark first each every letter of the dp matrix to be the False-->
        dp = [[False] * n for _ in range(n)]

        # mark each and every individual letter of the (s) to be palindromic -->
        # dp[i][i] = True-->
        for i in range(n):
            dp[i][i] = True

        start, max_len = 0, 1
        # start length from 2 --> (n + 1) time :O(n)
        for length in range(2, n + 1):
            # move i from 0 --> (n - length + 1) to upto which i can move for 
            # for checking string to be palindromic for required length-->
            # time : O(n)
            for i in range(n - length + 1):
                # calc : j last element for the substring : 
                # j = (start  to length - 1) to calc index for
                # for a substring of the appropriate length-->
                j = (i + length - 1)

                # check first && last index are same or not..
                # and if length of the substring is 2 or 
                # or subtstring in btw the sttring is also palindromic or not?
                if ((s[i] == s[j]) and ((length == 2) or (dp[i+1][j-1] == True))):
                    # if condn. matches --> check dp[i][j] = True-->
                    dp[i][j] = True
                    # mark start --> i
                    start = i
                    # mark max_len to the max_length -->
                    # via this condn..
                    if (max_len <= length):
                        max_len = length



        # mmaximum possible palindromic substring :
        # substring : s[start : start + max_len]-->
        # time : O(n ^ 2);
        # space : O(n ^ 2);
        return s[start:start + max_len]


        
        