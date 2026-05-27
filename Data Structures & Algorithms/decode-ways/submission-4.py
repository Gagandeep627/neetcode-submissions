class Solution:
    def numDecodings(self, s: str) -> int:


        # topic : (recursive ++ memoization approach)-->
        # count = 0
        memo = {}


        def helper(i, s, memo):

            if (i == len(s)):
                return 1

            if (s[i] == "0"):
                return 0

            if i in memo:
                return memo[i]

            count = helper(i + 1, s, memo)

            if ((i + 1 < len(s) )and (10 <= int(s[i:i+2]) <= 26)):
                count += helper(i + 2, s, memo)

            memo[i] = count
            return count 


        res = helper(0, s, memo)

#         ⏱️ Step 4: Time and Space Complexity
# Time → O(n)	Each index i (from 0 to len(s)) is solved once and stored in memo.
# Space → O(n)	Recursion stack + memo dictionary (one entry per index).


        return res

























        
        # topic : 1 D DP solutions -->(Not Brute Force Solution worked on so far)...
        # n = len(s)
        # # create a 1 D DP array-->
        # dp = [0] * (n + 1)
        # # set dp [n] --> 1 assigning intially decoding count of last string to be 
        # #  : 1
        # dp[n] = 1

        # # check each element from the last: time O(n)
        # for i in range(n-1, -1, -1):
        #     # if pointing --> 0 then no need to count it to dp[i] for decoding ways-->
        #     if s[i] == "0":
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i+1]
        #         # else : check if (that i + 1 (< n) like to check for the 2 string decoding pattern)
        #         # then length of the sub_string should be == 2 so for that only -->
        #         # at last our case didnt failed thats why condition for last member didnt lies out of 
        #         # the boundary && and the sub_string of length (2) --> 10 --> 26;
        #         if ((i + 1 < n) and (10 <= int(str(s[i:i+2])) <= 26)):
        #             # add dp[i] with the no. of decoding the other substrings in it (count)
        #             # to the dp[i]-->
        #             dp[i] += dp[i+2]

        # # return dp[0];
        # # time O(n), space : O(n)..
        # return dp[0]






        
        


