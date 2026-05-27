class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # topic : brute force solutions-->
        n = len(s)
        word_set = set(wordDict)
        memo = {}

        def can_break(i):

            if i == n:
                return True

            
            if i in memo:
                return memo[i]

            
            for word in wordDict:
                length = len(word)

                if s[i: i + length] == word and can_break(i + length):
                    memo[i] = True
                    return True

            

            memo[i] = False
            return False

        res = can_break(0)

        return res



            
            


        
        # Time :
        # O(n × 2ⁿ)
        # Each index can branch to many next indices → exponential growth
        res = can_break(0)
        return res





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





