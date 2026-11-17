class MinStack:

    def __init__(self):
        self.stack = []
        self.minPrefix = []
        self.curMin = float('inf')        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curMin = min(self.curMin, val)
        self.minPrefix.append(self.curMin)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minPrefix.pop()
        if not self.minPrefix:
            self.curMin = float('inf')
        else:
            self.curMin = self.minPrefix[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minPrefix[-1]
        
