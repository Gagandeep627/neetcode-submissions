class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        max_len = 0

        for i in range(n):
            for j in range(i + 1 ,n + 1):

                sub_string = s[i : j]

                if (len(set(sub_string)) == len(sub_string)):
                    max_len = max(max_len, len(sub_string))


        return max_len

























        



        #Topic : Sliding Window-->

        #Base Case-->
        # if len(set(s)) == 1:
        #     return 1 

        # left = 0
        # reoccur_set = set()
        # max_len = 0
        

        # #--> O(N)
        # for right in range(len(s)):


        #     while (s[right] in reoccur_set):
        #         reoccur_set.remove(s[left]) #
        #         left += 1



        #     reoccur_set.add(s[right])
        #     max_len = max(max_len , (right - left + 1))


        
        # #-->Time_Complexity : O(N)
        # return max_len


            

