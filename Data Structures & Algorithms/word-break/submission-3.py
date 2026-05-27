class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        



        # topic : Recursive ++ memoization code-->
        
        n = len(s)
        # removed overlapped words from worddict..
        word_set = set(wordDict)
        # creation for dp:
        memo = {}

        def can_break(i):
            
            # if start + some length had reached to == n:then return True 
            # for valid existance of that particular word in the word_set/ dict..
            if i == n:
                return True

            # if start + some length already in the memo 
            # return its boolean value calculated...
            if i in memo:
                return memo[i]

            # go to eacch word in the word_set
            for word in word_set:
                # take its length-->
                length = len(word)
                # check if its substring to it is == word if found true
                # call the recursive can_breaK() function to evaluate for
                # various substring with the various start values-->
                if s[i: i + length] == word and can_break(i + length):
                    # then after that start doing the backtrack 
                    # fucntion for the above code && to the each start 
                    # value it do had crossed then mark memo[i] = True;
                    # return True also to mark memo[i] = TRue
                    memo[i] = True
                    return True

            
            # if start + length != word
            # mark memo[i to which start gone] --> false 
            # return : false too..
            memo[i] = False
            return False
        
        # start for a call can_break(start : 0);
        res = can_break(0)
        # Time Complexity=O(n×m×t)
        # Space Complexity = O(n)
        # return : res;
        return res



            
            


        
        # Time :
        # O(n × 2ⁿ)
        # Each index can branch to many next indices → exponential growth
        res = can_break(0)
        return res




        # topic : brute force solutions-->
        # word_set = set(wordDict)

        # def can_break(start):

        #     if (start == len(s)):
        #         return True


        #     for end in range(start + 1, len(s) + 1):
        #         prefix = s[start: end]
        #         if prefix in word_set:
        #             if can_break(end):
        #                 return True

        #     return False


        
        # # Time :
        # # O(n × 2ⁿ)
        # # Each index can branch to many next indices → exponential growth
        # res = can_break(0)
        # return res





