class Solution:
    def evalRPN(self, tokens: List[str]) -> int:




        # method : stack
        # time complexity : O(N). : ??


        mapping_tokens = ["+","*","-",'/']
        stack = []


        for char in tokens:
            res = None
            if char in mapping_tokens and (len(stack) >= 2):
                s = stack.pop()
                f = stack.pop()
                if char == "+":
                    res = f + s
                elif char == "*":
                    res = f * s
                elif char == "-":
                    res = f - s
                else:
                    res = int(f / s)

                if res != None:stack.append(res) 

            else:
                integral_value = int(char)
                stack.append(integral_value)


        


        return (stack[-1] if stack else 0)






                












        