from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:




        if len(s) != len(t):
            return False

        
        ans = [0] * 26


        for i in range(0, len(s)):
            ans[ord(s[i]) - ord("a")] += 1

            ans[ord(t[i]) - ord("a")] -= 1



        # if its not an anagram -->

        for j in ans:
            if (j != 0):
                return False


        # else if its an anagram -->
        return True





        # Comparison is still O(n + m) time and
        #  O(1) extra space (since only 26 lowercase letters are possible).

        # return (Counter(s) == Counter(t))
        


        







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