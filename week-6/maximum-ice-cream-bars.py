class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        minVal = min(costs)
        maxVal = max(costs)
        counter = [0]*(maxVal-minVal+1)
        for cost in costs:
            counter[cost-minVal] += 1

        idx = 0
        for i in range(len(counter)):
            for j in range(counter[i]):
                if i+minVal <= coins:
                    idx += 1
                    coins -= (i+minVal)
                else:
                    return idx
        return len(costs)
                

      
