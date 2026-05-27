class Solution:
    def generateParenthesis(self, n: int) -> List[str]:



        result = []


        def backtracking(current, open_bracket, close_bracket):


            if len(current) == 2 * n:
                result.append(current)
                return


            if (open_bracket < n):
                backtracking(current + "(", open_bracket + 1, close_bracket)


            if (close_bracket < open_bracket):
                backtracking(current + ")", open_bracket, close_bracket + 1)










        backtracking("", 0, 0)
        return result

        
        