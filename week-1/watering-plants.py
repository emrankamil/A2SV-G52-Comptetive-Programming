class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total_water = capacity
        steps = 0
        for i in range(len(plants)):
            # 2*i steps are required to refill and get back to the place    and 1 additional step to proceed.
            if total_water - plants[i] < 0: 
                steps += 2*i+1
                total_water  = capacity - plants[i]
            else:
                steps += 1
                total_water -= plants[i]

        return steps
            