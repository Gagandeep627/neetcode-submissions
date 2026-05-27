class MinStack:

    def __init__(self):
        # time : o(1)
        self.stack = []
        self.min_stack = []

 
    def push(self, val: int) -> None:
         # time : o(1)
        # add val
        self.stack.append(val)

        if not (self.min_stack) or (self.min_stack[-1] >= val):
            self.min_stack.append(val)
        # elif (self.min_stack[-1] >= val):
        #     self.min_stack.append(val)


        

    def pop(self) -> None:
         # time : o(1)
        if len(self.stack) > 0:
            topp = self.stack.pop()
        
            if (self.min_stack[-1] == topp):
                self.min_stack.pop()


    def top(self) -> int:
         # time : o(1)
        topp = None
        if len(self.stack) > 0:
            topp = self.stack[-1]
        

        return int(topp)

    def getMin(self) -> int:
         # time : o(1)
        # min_val = None
        if self.min_stack:
            return self.min_stack[-1]
        else:
            min_val = None
            return min_val
        
