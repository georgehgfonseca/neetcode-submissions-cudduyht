class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixMin = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.prefixMin:
            self.prefixMin.append(min(self.prefixMin[-1], val))
        else:
            self.prefixMin.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.prefixMin.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.prefixMin[-1]
        
