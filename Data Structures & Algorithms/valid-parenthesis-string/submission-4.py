class Solution:
    def checkValidString(self, s: str) -> bool:



        # topic : brute force - recursive solutions:-

        n = len(s)

        memo = {}

        def dfs(i, c):
            
            if (i,c) in memo:
                return memo[(i,c)]

            if (c<0):
                return False

            if (i == (n)):
                if (c == 0):
                    return True
                else:
                    return False

            if (s[i] == "("):
                return dfs(i+1, c+1)
            
            if (s[i] == ")"):
                return dfs(i+1, c-1)

            

            try_valid = (

                dfs(i+1, c+1) or #treat * as "("
                dfs(i+1, c-1) or #treat * as ")"
                dfs(i+1, c) #treat * as "Empty"

            )

            memo[(i,c)] = try_valid

            return memo[(i,c)]


        start_index, open_count = 0, 0

        return dfs(start_index, open_count)
        