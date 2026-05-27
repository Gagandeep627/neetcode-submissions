class Solution:
    def isPalindrome(self, s: str) -> bool:
        # topic : 2 pointers -- approach -->
        

        # topic : optimal approach->
        # topic : 2 pointer approach:




        left = 0 #left pointer : 0
        right = len(s) - 1 # right pointer : len(s) - 1


        # loop untill left < right:
        while (left < right):
            # ~(1)
            #now check if s[left] in alphjanumeric is true
            # if yes increment left += 1
            # continue to other loop
            if not s[left].isalnum():
                left += 1
                continue

            
            if not s[right].isalnum():
                right -= 1
                continue

            
            if (s[left].lower() != s[right].lower()):
                return False

            
            left += 1
            right -= 1

















































































        # topic : brute force solutions:-



    
        newStr = '' #set newstr : "" empty_string
        
        
        # for each char in s:-
        for c in s:
            # now just check if char.isalphanumeric or not if
            # foun alphanumeric is YES
            # then add the char_lower case letter of the character
            # to the newstr
            if c.isalnum():
                # via syntax : newstr += c.lower()
                newStr += c.lower()

        # now check the newstr from the front and backwards
        # count as same or not if yes
        # then return True
        # otherwise : answer : False
        # return answer;
        return newStr == newStr[::-1]

        # topic : 2 pointers -- approach -->
        # space : o(1)
        left = 0
        # space : o(1)
        right = len(s) - 1


        # time : o(n)
        while (left < right):


            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            
            if (s[left].lower() != s[right].lower()):
                return False

            
            left += 1
            right -= 1




# 🧩 Complexity

# Time:   O(n) → Each character is visited at most once.

# Space: O(1) → No extra storage used (we use pointers only).


        
        return True










        