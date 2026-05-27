class Solution:
    def isValid(self, s: str) -> bool:


        # method 1 : stack...

        l1 = list(s)
        stack = []



        # brute force approach_to solve the problem...

        



        while (l1):

            num = l1.pop()
            if num in ([")", "}", "]"]) and num not in stack:
                stack.append(num)


            elif len(stack) == 0:
                stack.append(num)


            elif num == "{" and stack[-1] == "}" :
                stack.pop()

            elif num == "[" and stack[-1] == "]" :
                stack.pop()

            elif num == "(" and stack[-1] == ")" :
                stack.pop()

            else:
                return False

              

           
            


        

        return (len(stack) == 0) and len(l1) == 0

            

            

        