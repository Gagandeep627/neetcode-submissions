from collections import Counter
# import counter from collections:-

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        

        # Topic : Optimal_Solutions:-
        
        # if length(s) is not equal to length(t):
            # ans : False
        if len(s) != len(t):
            return False

        # there are 26 letters in characters frequecy:
        ans = [0] * 26
        
        
        # loop untill the range of length(s or t):-
        for i in range(0, len(s)):
            # evaluate (ord(s[i]) - ord("a")) : 1
            # ans[1] += 1
            ans[ord(s[i]) - ord("a")] += 1

            # evaluate (ord(t[i]) - ord("a")) : 2
            # ans[2] -= 1
            ans[ord(t[i]) - ord("a")] -= 1



        # if its not an anagram -->
        # loop untill every element in ans:-
        for j in ans:
            # if any char is not 0 in the ans:
            if (j != 0):
                # ans : False
                return False


        # else if its an anagram -->
        # ans : True;
        return True




        # topic : brute-force solutions :-

        #######
        # create two mapp-

#         # arr_t a map
#         arr_t = {}

#         # arr_s a map
#         arr_s = {}


# # O(n) : time : O(n)

#         # for each character in s:
#         for i in s:
#             #  if that specific (char : c) is not in arr_t:
#             if (i not in arr_t):
#                 # set arr_t[char entry] = 1
#                 arr_t[i] = 1
#             else:
#                 # else if already presented that particular character:
#                 # increment(arr_t[i] += 1)
#                 arr_t[i] += 1


# # o(m)  : time : O(m)
#         # same procedure may be get applied to t:
#         # map each and every entry for present in t in arr_s
#         # as entry count top be the counter (chars):- 
#         for i in t:
#             if (i not in arr_s):
#                 arr_s[i] = 1
#             else:
#                 arr_s[i] += 1


# # o(n + m) time : O(n + m)
#         # now check whether the map frequency of the both frequency_dictionary
#         # arr_t, arr_s are equal or not :
#         # if they are the our result : True
#         # else : our result is False
#         return (arr_t == arr_s)

        # this will indicate anagram is a string comtains exact
        #  same chars as anoher string , but the order of the chars can be 
        # varied:- // different..




        #########


        if len(s) != len(t):
            return False

        # time comp : o(n)
        # space comp : o(1)
        ans = [0] * 26


        # time comp : o(n)
        for i in range(0, len(s)):
            ans[ord(s[i]) - ord("a")] += 1

            ans[ord(t[i]) - ord("a")] -= 1



        # if its not an anagram -->
    # time comp : o(m)
        for j in ans:
            if (j != 0):
                return False

    # resultant time complex : o(n + m)
    # space comp : o(1)
        # else if its an anagram -->
        return True


    # correct solution , Move to nxt quesns..





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