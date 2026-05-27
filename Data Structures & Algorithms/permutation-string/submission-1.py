class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        # topic : brute force solution
        n = len(s1)

        #O(0 -- i) characters
        for i in range(0, len(s2) - n + 1):
            #O(i -- n) : O(n) characters
            sub = s2[i : i + n]
            # O(log(n) for m elements less than == len(s1) say of length m < len(s2) : m * log(n))
            if sorted(sub) == sorted(s1):
                return True

        
# Time_Complexity : O(n * m * log(n))
        return False
        