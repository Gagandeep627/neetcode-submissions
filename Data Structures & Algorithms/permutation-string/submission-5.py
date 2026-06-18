class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        

        
         # Topic : Sliding window Approach // Optimal Solution Approach.... ++ : ++ ??



        #if length(s1) > length(s2) : then permutation of the string s1
        # can't exist in s2 -->
        if len(s1) > len(s2):
            return False



        #s1_count is maintained....
        s1_count = [0] * 26

        #s2_count is maintained....
        s2_count = [0] * 26

        # count integer value to each character in the s1_count-->
        #O(n)
        for ch in s1:
            s1_count[ord(ch) - ord("a")] += 1


        
        # O(m = len(s2)) -->
        for j in range(len(s2)):
            #check the value of the variable += 1
            s2_count[ord(s2[j]) - ord("a")] += 1

            #if length of (j >= len(s1) : then remove the most left variable from  the sliding window)
            #// Move Left to += 1
            if (j >= len(s1)):
                s2_count[ord(s2[j - len(s1)]) - ord("a")] -= 1

            #if s1_count == s2_count then variables of the count for the s1 && s2 are same
            #so if they are same, then return True -->
            if s1_count == s2_count:
                return True

        # Time_complexity : O(n + m) : so m >= n : O(m) time complexity...
        # return False ->
        return False







# topic : brute force solutions required. : ??
        
        # n = len(s1)

        # for i in range(0, len(s2) - n + 1):
        #     sub = s2[i : i + n]

        #     if sorted(sub) == sorted(s1):
        #         return True

        

        # return False










































































        # Topic : Sliding window Approach // Optimal Solution Approach.... ++ : ++ ??


        
        #if length(s1) > length(s2) : then permutation of the string s1
        # can't exist in s2 -->
        if len(s1) > len(s2):
            return False


        #maintain a s1_count which will be s1_count : [0] * 26
        #s1_count is maintained....
        s1_count = [0] * 26
        
        # maintain s2_count for each and every characters which will be 
        # s2_count : [0] * 26
        #s2_count is maintained....
        s2_count = [0] * 26


        # for each character in s1:
        # count integer value to each character in the s1_count-->
        for ch in s1:
            # set s1_count[ord(ch) - ord("a")] += 1
            s1_count[ord(ch) - ord("a")] += 1


        
        # O(m = len(s2)) -->
        # for each char in range(length(s2)):-
        for j in range(len(s2)):
            #check the value of the variable += 1
            # s2_count[ord(s2)-ord("a")] += 1
            s2_count[ord(s2[j]) - ord("a")] += 1

            #if length of (j >= len(s1) : then remove the most left variable from  the sliding window)
            #// Move Left to += 1
            # now suppose if j exceeds the len(s1) at any particular 
            # point:-
            if (j >= len(s1)):
                # decrement the frequency count of the letter 
                # of that character to 1
                #  ~1 : freuency of new char : (ord(s2[j-len(s1)]) - ord("a")) -= 1 
                # in the s2_count (freq of the letter) -= 1
                # extra elements freq in the s2_character count 
                # removing / subducing it to 0 for extra elements rather than present in the s1:-
                
                # via syntax as this below:
                # s2_count(ord(s2[j-len(s1)]) - ord("a")) ~ deduce it by 1;
                s2_count[ord(s2[j - len(s1)]) - ord("a")] -= 1

            #if s1_count == s2_count then variables of the count for the s1 && s2 are same
            #so if they are same, then return True -->

            #  now do check after doing such kind of operations :
            # does the s1_count && s2_count matches with eacxh other or not..
            # if (yes) : answer : True
            # return answer;
            if s1_count == s2_count:
                return True


        # else : answer : False
        # return answer;
        # return False ->
        return False




































        # topic : brute force solutions:->
        # set n : length of s1
        n = len(s1)

        # loop i in range(0, length_of_string(s2) - (length_of_string(s1)) + 1)

        for i in range(0, len(s2) - n + 1):

            # evaluate sub_string : s2[i : i + n]
            sub = s2[i : i + n]


            # now check if the sorted(sub) && sorted(s1) 
            # is same or not if yes
            # then possible a pair of permutation of sub
            # exists in the s1: if (Yes):
            # answer : True
            # return True

            if sorted(sub) == sorted(s1):
                return True

        # return False

        return False
























































































        # Topic : Sliding window Approach // Optimal Solution Approach.... ++ : ++ ??

        # Topic : Sliding Window Approach // Optimal Solution Approach -->
        # Optimal Solutions __ Sliding Window Approach -->

        #if length(s1) > length(s2) : then permutation of the string s1
        # can't exist in s2 -->


        
        # if at any point length_s1 exceeds length_s2 then none of the sub_string in 
        # s2 : can validate to check permutations in s2 : ans : False
        # our result : False : 
        # return False
        if len(s1) > len(s2):
            return False

        ##


        # check s1_count which will be [0] * 26(no. of letters in the sub_array):-
        #s1_count is maintained....
        s1_count = [0] * 26
        

        # check s2_count which will be [0] * 26(no. of letters in the sub_array):-
        #s2_count is maintained....
        s2_count = [0] * 26


        #for every ch in s1:
        # count integer value to each character in the s1_count-->
        for ch in s1:
            # for every letter index though evaluated : ord(ch) - ord("a") 
            # increase_count_ch += 1
            s1_count[ord(ch) - ord("a")] += 1


        
        # O(m = len(s2)) -->
        # loop through each index in s_string:
        for j in range(len(s2)):

            # also do inc all letter equvalent to their char : index inc(+1)
            # maintain the freq for all chars for s2_count:-
            #check the value of the variable += 1
            s2_count[ord(s2[j]) - ord("a")] += 1

            #if length of (j >= len(s1) : then remove the most left variable from  the sliding window)
            #// Move Left to += 1

            # on condn 1:- if (j : (index in s2_string)  exceeds whole length_s1 or is equal to it):-

            if (j >= len(s1)):
                # now maintain s2_count equalent to s1: then remove left variable from the sliding window
                # move left += 1
                # s2_count[freq count of s2_left : s2_count[ord(s2[j - len(s1)]) - ord("a")] -= 1]
                s2_count[ord(s2[j - len(s1)]) - ord("a")] -= 1


            # now on condn suppose s1_count ==  s2_count: 
            # result : True, answer  : True --> return True
            #if s1_count == s2_count then variables of the count for the s1 && s2 are same
            #so if they are same, then return True -->
            if s1_count == s2_count:
                return True


        # return False ->
        return False


        











































        # Topic : Sliding window Approach // Optimal Solution Approach.... ++ : ++ ??
        #(Optimal solutions approach):-


        #if length(s1) > length(s2) : then permutation of the string s1
        # can't exist in s2 -->
        if len(s1) > len(s2):
            return False



        #s1_count is maintained....
        # as no. of chars // letters are 26:
        #s1_count is mainatained : [0] * 26
        s1_count = [0] * 26

        #s2_count is maintained.... similarlyy s2_count is made : [0] * 26
        s2_count = [0] * 26

        # count integer value to each character in the s1_count-->
        #O(n)
        for ch in s1:
            s1_count[ord(ch) - ord("a")] += 1


        
        # O(m = len(s2)) -->
        for j in range(len(s2)):
            #check the value of the variable += 1
            s2_count[ord(s2[j]) - ord("a")] += 1

            #if length of (j >= len(s1) : then remove the most left variable from  the sliding window)
            #// Move Left to += 1
            if (j >= len(s1)):
                s2_count[ord(s2[j - len(s1)]) - ord("a")] -= 1

            #if s1_count == s2_count then variables of the count for the s1 && s2 are same
            #so if they are same, then return True -->
            if s1_count == s2_count:
                return True

        # Time_complexity : O(n + m) : so m >= n : O(m) time complexity...
        # return False ->
        return False














        # topic : Brute force solutions :-

        #n : length of string (s1)
        n = len(s1)


        # loop till length_s2:
        # (length_s2 - n) + 1 to reach uptill (length_s2 - n) from 0 set as : index (i)
        for i in range(0, len(s2) - n + 1):# Because for each of the `(m - n + 1)` substrings
            # select every sub_string from s2
            # s2[from every i to (i + n)] : set as sub:-
            sub = s2[i : i + n]
            

            # sort each and every new checked sub with our original 
            # string : s1 and checked if found equal (value : True):-
            if sorted(sub) == sorted(s1): #we sort `n` characters (`O(n log n)`)
                return True #ans : True -> result : True;

        #**Time Complexity:** `O((m - n + 1) * n log n)` → simplifies to **O(m * n log n)**
        # if neither any of the sub_string found in the s1 : then return False;
        return False






        # topic : brute force solution (*brute force solutions):-
        #n : length of s1:-
        # n = len(s1)

        # #O(0 -- i) characters
        # loop uptill (m - n + 1):-
        # loop i in range(0, length of  s2 - length of s1 + 1)
        # for i in range(0, len(s2) - n + 1):
        #     #O(i -- n) : O(n) characters
        #     sub_string :- s2[i : i + n (length uptill sub_string of s1 can exists will be
        #will be checked uptill that ( so i -. i + n(length of sub_string (n)))..)]
        #     sub = s2[i : i + n] #loop uptill n
        #     # O(log(n) for m elements less than == len(s1) say of length m < len(s2) : m * log(n))
        # sorted(sub) and sorted(s1) if are equal means after sortion of both the strings alphjabetically 
        #got the same answer then : return True;
        #     if sorted(sub) == sorted(s1): #sorting of s1 : Log(n)
        #         return True

        
    # Time_Complexity : O(n * m * log(n))


#     ✅ **Time Complexity:** `O((m - n + 1) * n log n)` → simplifies to **O(m * n log n)**
# where:

# * `m` = length of `s2`
# * `n` = length of `s1`

# 👉 Because for each of the `(m - n + 1)` substrings, we sort `n` characters (`O(n log n)`).

        return False
        