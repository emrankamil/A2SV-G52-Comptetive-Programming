class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low+high)//2
            if high == low+1:
                print(mid)
            if self.checkValidity(mid, weights, days):
                high = mid
            else:
                low = mid+1
        return high
    
    def checkValidity(self, capacity, weights, days):
        cur_days = 0
        cur_weights = 0
        for weight in weights:
            cur_weights += weight
            if cur_weights == capacity:
                cur_days += 1
                cur_weights = 0
            elif cur_weights > capacity:
                cur_days += 1
                cur_weights = weight
        
        if cur_weights:
            return cur_days + 1<= days
        return cur_days <= days

