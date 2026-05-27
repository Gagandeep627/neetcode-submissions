class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Topic : Sliding window Approach // Optimal Solution Approach.... ++ : ++ ??



        #if length(s1) > length(s2) : then permutation of the string s1
        # can't exist in s2 -->
        if len(s1) > len(s2):
            return False



        #s1_count is maintained....
        s1_count = [0] * 26

        #s2_count is maintained....
        s2_count = [0] * 26

        # count integer value to each character in the s1_count-->
        #O(n)
        for ch in s1:
            s1_count[ord(ch) - ord("a")] += 1


        
        # O(m = len(s2)) -->
        for j in range(len(s2)):
            #check the value of the variable += 1
            s2_count[ord(s2[j]) - ord("a")] += 1

            #if length of (j >= len(s1) : then remove the most left variable from  the sliding window)
            #// Move Left to += 1
            if (j >= len(s1)):
                s2_count[ord(s2[j - len(s1)]) - ord("a")] -= 1

            #if s1_count == s2_count then variables of the count for the s1 && s2 are same
            #so if they are same, then return True -->
            if s1_count == s2_count:
                return True

        # Time_complexity : O(n + m) : so m >= n : O(m) time complexity...
        # return False ->
        return False























        # topic : brute force solution
        # n = len(s1)

        # #O(0 -- i) characters
        # for i in range(0, len(s2) - n + 1):
        #     #O(i -- n) : O(n) characters
        #     sub = s2[i : i + n]
        #     # O(log(n) for m elements less than == len(s1) say of length m < len(s2) : m * log(n))
        #     if sorted(sub) == sorted(s1):
        #         return True

        
    # Time_Complexity : O(n * m * log(n))


#     ✅ **Time Complexity:** `O((m - n + 1) * n log n)` → simplifies to **O(m * n log n)**
# where:

# * `m` = length of `s2`
# * `n` = length of `s1`

# 👉 Because for each of the `(m - n + 1)` substrings, we sort `n` characters (`O(n log n)`).

        return False
        