class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        



        #Topic : Sliding Window-->

        #Base Case-->
        if len(set(s)) == 1:
            return 1 

        left = 0
        reoccur_set = set()
        max_len = 0

        for right in range(len(s)):


            while (s[right] in reoccur_set):
                reoccur_set.remove(s[left]) #
                left += 1



            reoccur_set.add(s[right])
            max_len = max(max_len , (right - left + 1))


        

        return max_len


            

