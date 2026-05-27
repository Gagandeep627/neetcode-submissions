class Solution:
    def minWindow(self, s: str, t: str) -> str:


        # Topic : Brute Force.. ++ : ++ ??
        if not s or not t:
            return ""
        # O(n * m) : Checking each substring (character counts)	O(n * m)
        def covers(sub_string, t):
            
            for ch in t:
                if (sub_string.count(ch) < t.count(ch)):
                    return False

            return True



        min_substring = ""
        min_length = float("inf")

        # O(n)
        for i in range(0 , len(s)):
            # O(n)
            for j in range(i , len(s)):

                sub_string = s[i : j + 1]


                # O(n)
                if (covers(sub_string, t) == True):

                    if len(sub_string) < min_length:
                        min_length = len(sub_string)
                        min_substring = sub_string

        # time_complexity : O(n * n * n) : O(n ^ 3). ++ : ++ ??


        # ⏱️ Time & Space Complexity
# Step	Cost
# Generating all substrings	O(n²)
# Checking each substring (character counts)	O(n * m)
# Total Time Complexity	O(n³) (very slow)
        return min_substring

        