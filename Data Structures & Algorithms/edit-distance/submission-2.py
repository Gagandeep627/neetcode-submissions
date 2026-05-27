class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        # topic : recursive ++ memoized version solutions-->
        memo = {}

        def dfs(i, j):
            

            if (i,j) in memo:
                return memo[(i,j)]

            if (i == len(word1)):
                return len(word2) - j

            if (j == len(word2)):
                return len(word1) - i


            if (word1[i] == word2[j]):
                memo[(i,j)] = dfs(i+1, j+1)
                return memo[(i,j)]


            insert_cost = 1 + dfs(i,j+1)
            delete_cost = 1 + dfs(i + 1,j)
            replace_cost = 1 + dfs(i+1, j+1)



            ans = min(insert_cost, delete_cost, replace_cost)

            memo[(i,j)] = ans


            return ans

        
        s1, s2 = 0,0

        return dfs(s1, s2)

#         Time: O(m × n)

# Every state (i, j) is solved once.

# Space: O(m × n)

# For memo + recursion stack.





        # topic : recursive ++ brute force solutions-->

        # def dfs(i, j):


            
        #     if (i == len(word1)):
        #         return len(word2) - j

            
        #     if (j == len(word2)):
        #         return len(word1) - i


        #     if (word1[i] == word2[j]):
        #         return dfs(i+1, j+1)


        #     insert_cost = 1 + dfs(i,j+1)
        #     delete_cost = 1 + dfs(i + 1,j)
        #     replace_cost = 1 + dfs(i+1, j+1)



        #     ans = min(insert_cost, delete_cost, replace_cost)

        #     return ans

        
        # s1, s2 = 0,0

        # return dfs(s1, s2)




# Brute Force Time (Worst Case)
# O(3^(min(m, n)))


# Because at each mismatch you branch into 3 recursive calls.

# ❌ Brute Force Space
# O(m + n)


# due to recursion depth (call stack).
        
        