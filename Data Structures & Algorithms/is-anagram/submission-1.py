from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return (Counter(s) == Counter(t))
        


        







        # time complexity : with O(n + m) time



#         arr_t = {}
#         arr_s = {}


# # O(n)
#         for i in s:
#             if (i not in arr_t):
#                 arr_t[i] = 1
#             else:
#                 arr_t[i] += 1


# # o(m)
#         for i in t:
#             if (i not in arr_s):
#                 arr_s[i] = 1
#             else:
#                 arr_s[i] += 1


# # o(n + m)

#         return (arr_t == arr_s)



        # You should aim for a solution with O(n + m) time and O(1) space, where n is the length of the string s and m is the length of the string t.