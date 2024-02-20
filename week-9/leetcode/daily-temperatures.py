class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures) 
        
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx = stack.pop()
                temperatures[idx] = i-idx
            stack.append(i)
        for i in stack:
            temperatures[i] = 0
        
        return temperatures