class Solution:
    def countSubstrings(self, s: str) -> int:



        n = len(s)

        if n < 2:
            return 1

        # topic : (Non DP Approach) -->
        # 2 pointer expand around the center approach-->

        def expand(left, right):

            curr = 0
            # check cond if left should be >= 0 and right should
            # be < n && s[left] == s[right] as inside it are already been check by 
            # so check for outside too also
            # left += 1 pointer && right -= 1 pointer-->
             
            while (left >= 0 and right < n and s[left] == s[right]):
                # if cond satisfies inc curr += 1 
                # expand left to left and right to right-->
                curr += 1
                left -= 1
                right += 1

            
            return curr #return : curr-->


        total = 0 # set --> 0
        # i uptill length(n)-->
        for i in range(n):
            # for odd length expression palindromes -->
            total += expand(i, i)
            
            # for even length expression palindromes->
            total += expand(i, i + 1)


# Time	Each center expands up to O(n) → total 2n−1 centers → O(n²)	O(n²)
# Space	Only pointers and counters used	O(1)


        
        return total
















        