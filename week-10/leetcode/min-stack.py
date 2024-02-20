class MinStack:

    def __init__(self):
        self.minStack = []
        self.minVal = []
        
    def push(self, val: int) -> None:
        self.minStack.append(val)
        if self.minVal:
            self.minVal.append(min(val, self.minVal[-1]))
        else:
            self.minVal.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.minStack.pop():
            self.minVal.pop()
        
    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()