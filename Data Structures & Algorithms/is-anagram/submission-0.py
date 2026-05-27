class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        


        # time complexity : with O(n + m) time



        arr_t = {}
        arr_s = {}


# O(n)
        for i in s:
            if (i not in arr_t):
                arr_t[i] = 1
            else:
                arr_t[i] += 1


# o(m)
        for i in t:
            if (i not in arr_s):
                arr_s[i] = 1
            else:
                arr_s[i] += 1


# o(n + m)

        return (arr_t == arr_s)