class Solution:
    def checkValidString(self, s: str) -> bool:

        # topic : Greedy methods (Most  Optimal Solutions time :- O(N)):-
        #checking for validity of parenthesis string:-
        #minmum possible no. of open "(" at this point:
        low = 0 #We use only two integer variables: low and high.
        # maximum possible no. of open "(" at this point
        high = 0 #No stacks, arrays, recursion, or memo tables.

        # We traverse the string exactly once.
        # traverse the string via each chars:
        for ch in s:

            # open bracket:-
            # case 1:current chars is "(":
            if (ch == "("):
                #( must inc open count
                low += 1
                high += 1
            # close brack
            # case 2 : current chars is ")":
            elif (ch == ")"):
                #")" mujst dec open count
                low -= 1
                high -= 1

            #case3 : current chars is "*"
            elif (ch == "*"):
                #"*" acn act as ")", "(" or empty
                # so minimjum opens decrese, maximum opens increase
                # treat low as close:
                low -= 1 #treating * as )
                # treat high as open:
                high += 1 #treating * as (
            # Each character updates low and high using constant-time operations.
            #if even the max possible ( gores negative,
            # it means we have more ) than ( -> invalid string
            if (high < 0):
                return False

            #min possible ( COUNT should never ne negative 
            #we can always treat extra ) or * as empty()
            if (low < 0):
                low = 0

            # No nested loops, no recursion, no backtracking.

        
        #after processing entire string:
        #if min open count is zero, all ( can be matched:
        return low == 0

        # ⏳ Time Complexity = O(n), where n is the length of the string.
        # 💾 Space Complexity = O(1) (constant space).
            























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
        