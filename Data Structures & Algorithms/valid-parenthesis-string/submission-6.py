class Solution:
    def checkValidString(self, s: str) -> bool:

        # topic : Greedy methods:-


        low = 0
        high = 0


        for ch in s:

            # open bracket:-
            if (ch == "("):
                low += 1
                high += 1
            # close brack
            elif (ch == ")"):
                low -= 1
                high -= 1

            
            elif (ch == "*"):
                # treat low as close:
                low -= 1
                # treat high as open:
                high += 1

            if (high < 0):
                return False

            if (low < 0):
                low = 0

        

        return low == 0
            























        # topic : brute force - recursive solutions:-

        # n = len(s)
        # # Space is used in two places:
        # # Stores up to n² states:
        # memo = {}

        # # Maximum depth = length of string = n:
        # def dfs(i, c):
        #     # index ranges from 0 → n → (n + 1) states
        #     # openCount ranges from 0 → n → (n + 1) states
        #     # So total unique states: (n + 1) × (n + 1) ≈ n²
        #     if (i,c) in memo:
        #         return memo[(i,c)]

        #     if (c<0):
        #         return False

        #     if (i == (n)):
        #         if (c == 0):
        #             return True
        #         else:
        #             return False

        #     if (s[i] == "("):
        #         return dfs(i+1, c+1)
            
        #     if (s[i] == ")"):
        #         return dfs(i+1, c-1)

            

        #     try_valid = (

        #         dfs(i+1, c+1) or #treat * as "("
        #         dfs(i+1, c-1) or #treat * as ")"
        #         dfs(i+1, c) #treat * as "Empty"

        #     )

        #     memo[(i,c)] = try_valid

        #     return memo[(i,c)]
        #     # Each state is computed once, and each computation does constant work.


        # start_index, open_count = 0, 0
        # # ⏳ Total Time Complexity = O(n²)
        # # 🔥 Total Space Complexity = O(n²)

        # # (the memo table dominates)
        
        # return dfs(start_index, open_count)



        # ✅ Brute-Force Recursive Solution Complexity
        # For each '*', we branch into 3 recursive calls:
        # treat as '('

        # treat as ')'

        # treat as "" So the recursion tree has branching factor 3 and depth n.

        # 🔥 Worst-case Time Complexity : O(3^n)

#         💾 Space Complexity (Precise)

#         1️⃣ Recursion stack depth:

#         At most n recursive calls deep O(n)
#         2️⃣ No extra data structures used

# So:

# 🔥 Total Space Complexity
# O(n)
        