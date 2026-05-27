class Solution:
    def countSubstrings(self, s: str) -> int:



        n = len(s)

        if n < 2:
            return 1


        def expand(left, right):

            curr = 0

            while (left >= 0 and right < n and s[left] == s[right]):
                curr += 1
                left -= 1
                right += 1

            
            return curr


        total = 0
        for i in range(n):

            total += expand(i, i)

            total += expand(i, i + 1)


        
        return total
















        