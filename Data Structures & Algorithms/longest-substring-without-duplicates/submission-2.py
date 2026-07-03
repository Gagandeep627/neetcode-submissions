class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # topic : brutte force solutions :->
        # Topic : brute_force --> (brute force topic):-
        # n : length(s);
        # n : length of (s);
        n = len(s)

        # max_len : 0
        max_len = 0 #set max_len -> 0

        # loop till n

        # loop i in range(n):
        # O(n)
        for i in range(n):
            # loop start from j in (next(i), n + 1):-
            # O(n)
            # loop j in range(i + 1, n):
            for j in range(i + 1 ,n + 1):
                #check for the substring untill (i:j-1)
                # O((j-i) + 1)
                # check for each corrosponding sub_string[i:j]
                sub_string = s[i : j]
                #if checking with all the
                # non duplcates(sub_string) values_length == length of sub_string:
                #then evaluate the max_length via prev calculated with the new sub_string:-
                

                # if length of((all the unique values in the sub_string)) is equals to 
                # the length of the sub_string which is being evaluated in the function of 
                # lengthOfLongestSubstring(string s);
                
                # range of O(1 --> length of ((j-i)) + 1)
                if (len(set(sub_string)) == len(sub_string)):

                    # then evaluate the max_length which will be equal to :
                    # maximum of (max_len, length of sub_string);
                    max_len = max(max_len, len(sub_string))


        # answer : max_len
        # return answer;

        
        #return max_length of the sub_string calculated so far...
        return max_len #2 loops -> O(n ^ 2);

























        


        # topic (Optimal_Solutions):-
        #Topic : Sliding Window-->

        #Base Case-->
        if len(set(s)) == 1:
            return 1 
        #set left : 0 index : 0
        left = 0
        # empty_set creation (non duplicates values):-
        reoccur_set = set()
        max_len = 0
        

        #--> O(N)
        # loop right from 0 -> len(s):
        for right in range(len(s)):

            #untill string(right : indexed is in our reoccur set):
            while (s[right] in reoccur_set):
                #remove the left most element from the R set  bcz
                # left most element in the set would be matching to right most element
                # as : like z from 0 indexed as left would match with 3 index : (z)
                # with the rightest index : "z"
                #so  remove the left : indexed string and 
                # increase our window from left += 1;
                reoccur_set.remove(s[left]) #
                left += 1


            # add the string (s[right]) in the our empty set:
            reoccur_set.add(s[right])
            #evaluate max_len :- as max(max_len , (length of substring : (right - left + 1)))
            max_len = max(max_len , (right - left + 1))


        
        #-->Time_Complexity : O(N)
        # our answer is : max_len 
        # return result : max_len == final evaluated answer:-;
        return max_len


            

