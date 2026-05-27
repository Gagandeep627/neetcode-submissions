class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
        if ((len(s1) + len(s2)) != len(s3)):
            return False

        memo = {} #1️⃣ Memo Dictionary: O(m × n) # (memo cache)-->

        # topic : recursive ++ memoizations solutions # (top - down dp solutions)-->


        # The DP state is defined as (i, j)
        def dfs(i, j): #2️⃣ Recursion Call Stack: O(m + n)
            
            # base case-->
            if (i,j) in memo:
                return memo[(i,j)]
            # if we consumed all characters from s1 and s23, 
            # and length matched earkier, this means success ->
            if ((i == len(s1)) and (j == len(s2))):
                return True

            k = (i + j) #current index : match in s3->

            # option 1: pick next letter from s1 (try matching from s1)
            # i can take 0 … m values → m + 1
            if ((i < len(s1)) and (s1[i] == s3[k])):
                if dfs(i+1,j):
                    memo[(i,j)] = True
                    return True

            # option 2: pick next letter from s1-> #(try matching from s2)
            # j can take 0 … n values → n + 1
            if (j < len(s2) and (s2[j] == s3[k])):
                if dfs(i, j+1):
                    memo[(i,j)] = True
                    return True

            # Each (i, j) is computed once, and after that returned from memo in O(1)
            # (m + 1) × (n + 1) = O(mn)
            # Time = O(mn)
            


#             Space : O(m × n)   (memo table)
# + O(m + n) (call stack)
# = O(m × n) overall
            # if no option works-> (no possible match)->
            memo[(i,j)] = False
            return False

        start1, start2 = 0,0

        # Time Complexity: O(m * n)
        # Space Complexity:O(m * n)

        return dfs(start1,start2)






        #For Brute force concept:

#         Time Complexity:
# O(2^(m + n))


# You branch two ways many times → exponential.

# Space Complexity:
# O(m + n)


# Due to recursion depth.


            




