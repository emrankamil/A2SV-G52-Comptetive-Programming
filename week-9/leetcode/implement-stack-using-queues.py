class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return 
        for i in range(len(self.queue)-1):
           self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)
        

    def top(self) -> int:
        if self.empty():
            return 
        for i in range(len(self.queue)-1):
           self.queue.append(self.queue.pop(0))
        val = self.queue.pop(0)
        self.queue.append(val)
        return val
        

    def empty(self) -> bool:
        return not len(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()