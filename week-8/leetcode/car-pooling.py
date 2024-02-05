class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        max_dis = max(trips, key=lambda x:x[2])[2]
        
        path = [0] * (max_dis + 1)
        for trip in trips:
            path[trip[1]] += trip[0]
            path[trip[2]] -= trip[0]  

        cumulative = 0
        for i in range(len(path)):
            cumulative += path[i]
            if cumulative > capacity:  
                return False

        return True