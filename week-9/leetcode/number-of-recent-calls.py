class RecentCounter:

    def __init__(self):
       self.stack = [] 

    def ping(self, t: int) -> int:
        self.stack.append(t)
        while self.stack[-1]-self.stack[0]>3000:
                self.stack.pop(0)
        return len(self.stack)
        
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)