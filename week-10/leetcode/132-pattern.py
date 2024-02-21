class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        monoStack = []
        minNum = nums[0]

        for i in nums[1:]:
            while monoStack and i >= monoStack[-1][0]:
                monoStack.pop()
            if monoStack and i > monoStack[-1][1]:
                return True
            monoStack.append([i, minNum])
            minNum = min(minNum, i)
        return False