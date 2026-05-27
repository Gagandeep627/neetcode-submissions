class MinStack:

    def __init__(self):
        self.stack = []

        
        

    def push(self, val: int) -> None:

        # add val
        self.stack.append(val)
        

    def pop(self) -> None:

        if len(self.stack) > 0:
            self.stack.pop()
\
    def top(self) -> int:

        topp = None
        if len(self.stack) > 0:
            topp = self.stack[-1]
        

        return int(topp)

    def getMin(self) -> int:

        min_val = None
        if len(self.stack) > 0:
            min_val = min(self.stack)


        return min_val
        
