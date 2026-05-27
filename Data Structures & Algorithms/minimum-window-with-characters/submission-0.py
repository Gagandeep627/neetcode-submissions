class Solution:
    def minWindow(self, s: str, t: str) -> str:



        if not s or not t:
            return ""

        def covers(sub_string, t):

            for ch in t:
                if (sub_string.count(ch) < t.count(ch)):
                    return False

            return True



        min_substring = ""
        min_length = float("inf")


        for i in range(0 , len(s)):
            for j in range(i , len(s)):

                sub_string = s[i : j + 1]



                if (covers(sub_string, t) == True):

                    if len(sub_string) < min_length:
                        min_length = len(sub_string)
                        min_substring = sub_string


        return min_substring

        